# employee_management/urls.py

from django.contrib import admin
from django.urls import path, include
from JobListings.views import show_resume, mail_send
from email_sender.views import show_mail_attachment

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the admin_panel URLs
    path('admin_panel/', include('admin_panel.urls')),
    path('', include('frontend_app.urls')),
    path('resumes/<str:resume_name>/', show_resume),
    path('attachments/<str:attachment_name>/', show_mail_attachment),
    path('mail/', mail_send),
    # Add other project-specific URLs here
]
