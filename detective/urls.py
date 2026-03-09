from django.urls import path
from . import views

app_name = 'detective'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.student_login, name='student_login'),
    path('logout/', views.student_logout, name='student_logout'),
    path('schema/', views.schema, name='schema'),
    path('investigate/', views.investigate, name='investigate'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),
    path('start-lock/', views.start_investigation, name='start_investigation'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('tab-switch/', views.record_tab_switch, name='record_tab_switch'),
]
