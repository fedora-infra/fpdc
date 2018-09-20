from rest_framework import viewsets
from rest_framework import filters

from fpdc.releases.models import Release
from fpdc.releases.serializers import ReleaseSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = "__all__"
    ordering = ("id",)
