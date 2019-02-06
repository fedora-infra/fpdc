from rest_framework.serializers import ModelSerializer, URLField

from fpdc.components.models import RPMPackage, Module, Container


class RPMPackageSerializer(ModelSerializer):
    dist_git_url = URLField(required=False, max_length=200)

    class Meta:
        model = RPMPackage
        fields = "__all__"


class ModuleSerializer(ModelSerializer):
    dist_git_url = URLField(required=False, max_length=200)

    class Meta:
        model = Module
        fields = "__all__"


class ContainerSerializer(ModelSerializer):
    dist_git_url = URLField(required=False, max_length=200)

    class Meta:
        model = Container
        fields = "__all__"
