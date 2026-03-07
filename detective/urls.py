from django.urls import path
from . import views

app_name = 'detective'

urlpatterns = [
    path('', views.home, name='home'),
    path('schema/', views.schema, name='schema'),
    path('investigate/', views.investigate, name='investigate'),
    path('start-lock/', views.start_investigation, name='start_investigation'),
    path('tab-switch/', views.record_tab_switch, name='record_tab_switch'),
]
