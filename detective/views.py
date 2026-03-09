from django.shortcuts import render, redirect
from django.db import connection
from django.http import JsonResponse
from .models import Participant
import re
import time

def home(request):
    return render(request, 'detective/home.html')

def student_login(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        password = request.POST.get('password')
        if password == 'shield123' and student_name:
            request.session['student_name'] = student_name
            request.session['student_auth'] = True
            # Automatically start investigation session
            request.session['start_time'] = time.time()
            request.session['is_started'] = True
            request.session['switch_count'] = 0
            request.session['is_disqualified'] = False
            return redirect('detective:investigate')
        else:
            return render(request, 'detective/login.html', {'error': 'Invalid Access Code'})
    return render(request, 'detective/login.html')

def student_logout(request):
    request.session.flush()
    return redirect('detective:home')

def schema(request):
    return render(request, 'detective/schema.html')

def start_investigation(request):
    """Initialize the 45-minute investigation session."""
    if request.method == 'POST':
        request.session['start_time'] = time.time()
        request.session['is_started'] = True
        request.session['switch_count'] = 0
        request.session['is_disqualified'] = False
        return JsonResponse({'status': 'success', 'start_time': request.session['start_time']})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def record_tab_switch(request):
    """Record a tab switch incident (MAX 2 strikes)."""
    if request.method == 'POST' and request.session.get('is_started'):
        count = request.session.get('switch_count', 0) + 1
        request.session['switch_count'] = count
        if count >= 2:
            request.session['is_disqualified'] = True
        return JsonResponse({'status': 'success', 'count': count, 'disqualified': request.session['is_disqualified']})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def investigate(request):
    if not request.session.get('student_auth'):
        return redirect('detective:student_login')
        
    is_started = request.session.get('is_started', False)
    start_time = request.session.get('start_time', 0)
    is_disqualified = request.session.get('is_disqualified', False)
    
    # Check for time-up
    current_time = time.time()
    time_limit = 45 * 60 # 45 minutes
    is_time_up = False
    time_remaining = time_limit
    
    if is_started:
        elapsed = current_time - start_time
        if elapsed > time_limit:
            is_time_up = True

    query = request.POST.get('query', '')
    if query:
        request.session['last_query'] = query
    elif request.method == 'GET':
        query = request.session.get('last_query', '')
        
    results = None
    error = None
    columns = None

    if request.method == 'POST' and not is_time_up and not is_disqualified and is_started:
        # Security check: Allow only SELECT queries
        if not re.match(r'^\s*SELECT', query, re.IGNORECASE):
            error = "Access Denied: Only SELECT queries are permitted by SHIELD Protocol."
        else:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    columns = [col[0] for col in cursor.description]
                    results = cursor.fetchall()
            except Exception as e:
                error = str(e)

    context = {
        'query': query,
        'results': results,
        'columns': columns,
        'error': error,
        'is_submitted': request.session.get('is_submitted', False),
    }
    return render(request, 'detective/investigate.html', context)

def submit_answer(request):
    if request.method == 'POST' and request.session.get('student_auth'):
        if request.session.get('is_submitted'):
            return JsonResponse({'status': 'error', 'message': 'Submission already recorded.'}, status=400)
            
        planner_name = request.POST.get('planner_name')
        student_name = request.session.get('student_name', 'Unknown')
        start_time = request.session.get('start_time', 0)
        completion_time = int(time.time() - start_time)
        
        # Save to database
        Participant.objects.create(
            student_name=student_name,
            planner_answer=planner_name,
            completion_time=completion_time
        )
        
        request.session['is_submitted'] = True
        return JsonResponse({'status': 'success', 'message': 'Submitted successfully'})
        
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def admin_login(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == 'altronix26':
            request.session['admin_auth'] = True
            return redirect('detective:admin_dashboard')
        else:
            return render(request, 'detective/admin_login.html', {'error': 'Unauthorized Access'})
    return render(request, 'detective/admin_login.html')

def admin_dashboard(request):
    if not request.session.get('admin_auth'):
        return redirect('detective:admin_login')
    
    participants = Participant.objects.all().order_by('completion_time')
    return render(request, 'detective/admin_dashboard.html', {'participants': participants})
