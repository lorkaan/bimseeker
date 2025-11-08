from django.db import models

from marketplace.accounts.models import User
from marketplace.tags.models import Tag

# Create your models here.
class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

class ContractorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
