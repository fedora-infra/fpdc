from rest_framework.serializers import ModelSerializer

from fpdc.releases.models import Release


class ReleaseSerializer(ModelSerializer):
    class Meta:
        model = Release
        fields = "__all__"
