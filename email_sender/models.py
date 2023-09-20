from django.db import models
from JobListings.models import Applicant
from GSS_Tenant.settings import EMAIL_HOST_USER


class Email_Compose(models.Model):
    # id = models.PositiveBigIntegerField(primary_key=True)
    subject = models.CharField(max_length=255)
    recipients = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    message = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    send_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
