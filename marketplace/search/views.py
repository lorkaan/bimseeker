from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Job
from services.models import ServiceListing
from profiles.models import ContractorProfile

class GlobalSearchView(APIView):
    def get(self, request):
        q = request.GET.get('q', '')
        jobs = Job.objects.filter(Q(title__icontains=q) | Q(tags__name__icontains=q)).distinct()
        services = ServiceListing.objects.filter(Q(title__icontains=q) | Q(tags__name__icontains=q)).distinct()
        contractors = ContractorProfile.objects.filter(Q(business_name__icontains=q) | Q(tags__name__icontains=q)).distinct()
        return Response({
            "jobs": [j.title for j in jobs],
            "services": [s.title for s in services],
            "contractors": [c.business_name for c in contractors],
        })
