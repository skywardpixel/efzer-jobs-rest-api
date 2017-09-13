from rest_framework import serializers
from rest_framework.reverse import reverse

from jobs.models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = [
            'url',
            'id',
            'published',
            'type',
            'company',
            'location',
            'job_position',
            'department',
            'publisher_class',
            'publisher',
            'salary',
            'submitting_resume',
            'description',
            'requirements',
            'company_description'
        ]

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('job-detail', kwargs={'pk': obj.pk}, request=request)
        }