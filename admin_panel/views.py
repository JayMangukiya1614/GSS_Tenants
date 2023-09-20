from django.shortcuts import render

# Create your views here.
# admin_panel/views.py

from django.contrib.auth.decorators import user_passes_test

def is_hr(user):
    return user.groups.filter(name='HR').exists()

def is_management(user):
    return user.groups.filter(name='Management').exists()

@user_passes_test(is_hr)
def hr_dashboard(request):
    # HR-specific functionality
    pass

@user_passes_test(is_management)
def management_dashboard(request):
    # Management-specific functionality
    pass
