import time

def investigation_status(request):
    """
    Context processor to provide investigation status to all templates.
    """
    is_started = request.session.get('is_started', False)
    start_time = request.session.get('start_time', 0)
    is_disqualified = request.session.get('is_disqualified', False)
    switch_count = request.session.get('switch_count', 0)
    
    # Calculate time remaining
    current_time = time.time()
    time_limit = 45 * 60 # 45 minutes
    is_time_up = False
    time_remaining = time_limit
    
    if is_started:
        elapsed = current_time - start_time
        time_remaining = max(0, time_limit - elapsed)
        if elapsed > time_limit:
            is_time_up = True
            
    return {
        'is_started': is_started,
        'is_disqualified': is_disqualified,
        'is_time_up': is_time_up,
        'time_remaining': int(time_remaining),
        'switch_count': switch_count,
    }
