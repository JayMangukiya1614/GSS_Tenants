from django.core.mail import send_mail, EmailMessage
from GSS_Tenant.settings import EMAIL_HOST_USER
from django.shortcuts import render
from django.http import FileResponse, HttpResponse

# Create your views here.


def show_resume(request, resume_name):
    file = 'resumes/' + resume_name
    try:
        with open(file, 'rb') as pdf_file:
            response = HttpResponse(
                pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
            return response
            # response = FileResponse(pdf_file, content_type='application/pdf')
            # response['Content-Disposition'] = f'inline; filename="{file}"'
            # return response
    except FileNotFoundError:
        return HttpResponse('file_not_found.html')


def mail_send(request):
    send_mail(from_email=EMAIL_HOST_USER, subject='test_mail', message='Hi',
              recipient_list=['siddhantkhannamailbox@gmail.com'], fail_silently=True)
    return HttpResponse('mail sent')
