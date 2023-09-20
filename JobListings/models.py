from django.db import models

class JobListing(models.Model):
    currently_accepting = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    description_file = models.FileField(upload_to='static/jd/')

    def __str__(self) -> str:
        return self.title

class Applicant(models.Model):
    selected = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    linkedin_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    applied_for = models.ForeignKey(JobListing, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"

class ApplicantProgress(models.Model):
    APPLICANT_STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('in_review', 'In Review'),
        ('interviewing', 'Interviewing'),
        ('offer_extended', 'Offer Extended'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
    ]
    selected = models.BooleanField(default=False)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=APPLICANT_STATUS_CHOICES, default='applied'
    )
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.applicant.name} - {self.status}"