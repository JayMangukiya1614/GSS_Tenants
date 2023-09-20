from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class Client(TenantMixin):
    name = models.CharField(max_length=100)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass


# class JobListing(models.Model):
#     currently_accepting = models.BooleanField(default=True)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     description_file = models.FileField(upload_to='static/jd/')

#     def __str__(self) -> str:
#         return self.title