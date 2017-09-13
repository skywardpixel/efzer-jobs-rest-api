from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from jobs import views

schema_view = get_schema_view(title="EFZer Jobs API")

router = DefaultRouter()
router.register(r'jobs', views.JobViewSet)

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]