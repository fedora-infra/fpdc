from rest_framework import viewsets
from rest_framework import filters

from fpdc.releases.models import ReleaseType
from fpdc.releases.serializers import ReleaseTypeSerializer


class ReleaseTypeViewSet(viewsets.ModelViewSet):
    queryset = ReleaseType.objects.all()
    serializer_class = ReleaseTypeSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = "__all__"
    ordering = ("id",)
