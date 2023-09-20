from django.shortcuts import render
from django.http import FileResponse,HttpResponse

# Create your views here.

def show_mail_attachment(request, attachment_name):
    file = 'attachments/' + attachment_name
    try:
        with open(file, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
            return response
            # response = FileResponse(pdf_file, content_type='application/pdf')
            # response['Content-Disposition'] = f'inline; filename="{file}"'
            # return response
    except FileNotFoundError:
        return HttpResponse('file_not_found.html')
