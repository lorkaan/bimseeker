from django.db import models

from marketplace.profiles.models import ContractorProfile
from marketplace.tags.models import Tag

# Create your models here.
class ServiceListing(models.Model):
    contractor = models.ForeignKey(ContractorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    price_range = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=255, blank=True)
    available = models.BooleanField(default=True)
