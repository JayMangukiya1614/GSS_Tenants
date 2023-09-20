from django.contrib import admin
# from applicants.models import Applicant
from JobListings.models import JobListing, Applicant, ApplicantProgress
from django.core.mail import send_mail, EmailMessage
from GSS_Tenant.settings import EMAIL_HOST_USER
from email_sender.models import Email_Compose
from django import forms
from JobListings.signals import send_notification_email  # Import your signal
from client.models import *
from django.contrib.auth.models import User  # Assuming you are using the User model



# if 'admin' in [user.username for user in admin.site._registry]:
#     admin.site.register(Client)



# class ClientAdmin(admin.ModelAdmin):
#     print("here")
#     def get_form(self, request):
#         if (request.user.username).lower() == 'admin' :
#             admin.site.register(Client)
#             admin.site.register(Domain)
    
#     get_form()


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email_Compose
        fields = '__all__'


@admin.register(Email_Compose)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'recipients', 'attachment',)
    list_filter = ('subject',)
    search_fields = ('subject', 'recipients',)
    form = EmailForm


def mail_send():
    send_mail(from_email=EMAIL_HOST_USER, subject='test_mail', message='Hi',
              recipient_list=['siddhantkhannamailbox@gmail.com'], fail_silently=True)


class ApplicantProgressInline(admin.TabularInline):
    model = ApplicantProgress
    extra = 0


admin.site.register(JobListing)


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'applied_for', 'selected')
    actions = ['send_email_action']
    inlines = [ApplicantProgressInline]

    def send_email_action(self, request, queryset):
        subject = 'Your job application status'
        message = 'Your job application status has been updated.'
        from_email = 'siddhantethansrec@example.com'  # Set your email address
        recipient_list = [applicant.email for applicant in queryset]
        print(recipient_list)

        # Send emails to selected applicants
        for applicant in queryset:
            send_mail(subject, message, from_email, [applicant.email])
            # send_notification_email(applicant.progress_set.latest('date_updated'))

        self.message_user(
            request, f'Emails sent to {len(queryset)} applicants.')

    send_email_action.short_description = 'Send email to selected applicants'

    # Add other customizations for the Applicant model
if "(name='admin')" in str(admin.site._registry):
    admin.site.register(Client)

