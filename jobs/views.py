from rest_framework import viewsets, permissions

from jobs.models import Job
from jobs.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Job.objects.order_by('date_published')
    serializer_class = JobSerializer
