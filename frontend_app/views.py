from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from JobListings.models import *
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
import os
from django.contrib.auth.models import User


# Create your views here.
def show_jd(request, jd_file_name):
    file = 'static/jd' + jd_file_name
    try:
        with open(file, 'rb') as pdf_file:
            response = HttpResponse(
                pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
            return response
    except FileNotFoundError:
        return redirect('/notfound')

        # return HttpResponse('file_not_found.html')


def index(request):
    return render(request, 'frontend_design/index.html')


def about(request):
    return render(request, 'frontend_design/about.html')


def services(request):
    return render(request, 'frontend_design/services.html')


def contact(request):
    return render(request, 'frontend_design/contact.html')


def career(request):
    # data = JobListing.objects.all()
    try:
        data = {
            'joblisting': JobListing.objects.all()
        }
        return render(request, 'frontend_design/career.html', data)
    except Exception as e:
        data = {
            'joblisting': None
        }
        return render(request, 'frontend_design/career.html', data)

def notfound(request):
    return render(request, 'frontend_design/404notfound.html')

# @require_POST


def job_opening_form(request, job_id):
    try:
        job_listing = JobListing.objects.get(id=job_id)
        # title = job_listing.title
        data = {
            'title': job_listing.title,
            'description_file': job_listing.description_file
        }
        return render(request, 'frontend_design/job_opening_form.html', data)

    except JobListing.DoesNotExist:
        return redirect('/notfound')


@csrf_protect
def get_job_form(request):
    if request.method == 'POST':
        applied_for_title = request.POST.get('applied_for')

        try:
            applied_for_job = JobListing.objects.get(title=applied_for_title)
        except JobListing.DoesNotExist:
            return HttpResponseNotFound("Job listing does not exist")

        resume = request.FILES.get('resume')

        if resume:
            # Generate a unique filename using timestamp and original filename
            timestamp = timezone.now().strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f"{timestamp}_{resume.name}"

            resume_folder_path = 'resumes/'
            file_path = os.path.join(resume_folder_path, file_name)

            lfs = FileSystemStorage(location=resume_folder_path)
            lfs.save(file_name, resume)

            # Create an Applicant object and save it to the database
            applicant = Applicant(
                selected=False,
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                resume='resumes/' + file_name,
                linkedin_profile=request.POST.get('linkedin_profile'),
                github_profile=request.POST.get('github_profile'),
                applied_for=applied_for_job
            )
            applicant.save()

            messages.success(request, "Form Successfully Filled Up")
            # Redirect to the home page or a different URL
            return redirect('/')

    return redirect('/notfound')


# def team(request):
#     return render(request, 'frontend_design/team.html')


def SignUp(request):
    return render(request, 'frontend_design/SignUp.html')


@csrf_protect
def signup_save(request):

    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    # return HttpResponse(password1)
    # Use keyword arguments to create the user
    user_ = User.objects.create(username=username, email=email, password=password1, is_staff=True)
    
    # Note: You should hash the password before saving it to the database.
    # You can use the set_password method to do that.
    user_.set_password(password1)
    
    user_.save()
    
    return HttpResponse('Work')

    
    
