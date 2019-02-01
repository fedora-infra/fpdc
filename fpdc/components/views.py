from rest_framework import viewsets
from rest_framework import filters

from fpdc.components.models import RPMPackage
from fpdc.components.serializers import RPMPackageSerializer


class RPMPackageViewSet(viewsets.ModelViewSet):
    queryset = RPMPackage.objects.all()
    serializer_class = RPMPackageSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = "__all__"
