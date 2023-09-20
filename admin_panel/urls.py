# admin_panel/urls.py
from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('management_dashboard/', views.management_dashboard, name='management_dashboard'),
    # Add more URLs for other custom admin panel views as needed
]
