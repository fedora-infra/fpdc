from rest_framework.serializers import ModelSerializer

from fpdc.releases.models import ReleaseType


class ReleaseTypeSerializer(ModelSerializer):
    class Meta:
        model = ReleaseType
        fields = "__all__"
