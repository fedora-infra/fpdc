from rest_framework import viewsets
from rest_framework import filters

from fpdc.components.models import RPMPackage, Module
from fpdc.components.serializers import RPMPackageSerializer, ModuleSerializer


class RPMPackageViewSet(viewsets.ModelViewSet):
    queryset = RPMPackage.objects.all()
    serializer_class = RPMPackageSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = "__all__"


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = "__all__"
