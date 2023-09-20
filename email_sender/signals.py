# job_listings/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Applicant, Email_Compose
from django.core.mail import send_mail, EmailMessage
from GSS_Tenant.settings import EMAIL_HOST_USER
# from admin_panel.admin import mail_send

@receiver(post_save, sender=Email_Compose)
def send_notification_email(sender, instance, **kwargs):
    # print(sender.APPLICANT_STATUS_CHOICES)
    print(instance)
    key = int(instance.id)
    mail_obj =  Email_Compose.objects.get(id=key)
    
    subject = mail_obj.subject
    message = mail_obj.message

    applicant_name = mail_obj.recipients
    # print(applicant_name)
    # applicant_obj = Applicant.objects.get(name=applicant_name)
    # email_add = applicant_obj.email
    email_add = str(applicant_name).split('-')[-1].strip()
    attachment = mail_obj.attachment

    # Send email with or without attachment
    if attachment:
        email = EmailMessage(subject, message, to=[email_add])
        email.attach(attachment.name, attachment.read())
        email.send()
    else:
        send_mail(subject, message, from_email=EMAIL_HOST_USER, recipient_list=[email_add], fail_silently=False)
