from rest_framework.serializers import ModelSerializer, URLField

from fpdc.components.models import RPMPackage


class RPMPackageSerializer(ModelSerializer):
    dist_git_url = URLField(required=False, max_length=200)

    class Meta:
        model = RPMPackage
        fields = "__all__"
