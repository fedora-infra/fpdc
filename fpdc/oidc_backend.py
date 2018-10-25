from django.conf import settings
from django.contrib.auth.models import Group
from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class FpdcOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        """
        Custom create_user method that sync the FAS releng-team member
        with the internal FPDC releng-group.
        """
        user = super(FpdcOIDCAuthenticationBackend, self).create_user(claims)

        if settings.FAS_GROUP in claims.get("groups", ""):
            releng_group, created = Group.objects.get_or_create(name="releng-team")
            releng_group.user_set.add(user)

        return user
