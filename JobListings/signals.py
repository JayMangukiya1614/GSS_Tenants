# job_listings/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ApplicantProgress, Applicant
from django.core.mail import send_mail
# from admin_panel.admin import mail_send

@receiver(post_save, sender=ApplicantProgress)
def send_notification_email(sender, instance, **kwargs):
    # print(sender.APPLICANT_STATUS_CHOICES)
    print(instance)
    temp = str(instance).split('-')
    applicant_name = temp[0].strip()
    status = temp[-1].strip().upper()
    # print(applicant_name, stage, status)

    applicant_obj = Applicant.objects.get(name=applicant_name)
    email_add = applicant_obj.email
    applied_for = applicant_obj.applied_for

    print(email_add, applied_for)

    subject = 'Your job application status'
    message = f'Dear {applicant_name}, Your job application status has been updated to {status}'
    from_email = 'siddhantethansrec@example.com'

    send_mail(subject, message, from_email, [email_add])
    
