from rest_framework import viewsets
from rest_framework import filters

from fpdc.releases.models import Release
from fpdc.releases.serializers import ReleaseSerializer


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = "__all__"
    ordering = ("-version",)  # Descending ordering on version higher version first.

    def get_queryset(self):
        """
        Optionally restricts the returned Release to only active releases,
        by filtering against a `active` query parameter in the URL.
        """
        queryset = Release.objects.all()
        active = self.request.query_params.get("active", None)
        if active is not None:
            queryset = queryset.filter(active=active.title())

        return queryset
