from rest_framework import viewsets

from fpdc.releases.models import ReleaseType
from fpdc.releases.serializers import ReleaseTypeSerializer


class ReleaseTypeViewSet(viewsets.ModelViewSet):
    queryset = ReleaseType.objects.all()
    serializer_class = ReleaseTypeSerializer
