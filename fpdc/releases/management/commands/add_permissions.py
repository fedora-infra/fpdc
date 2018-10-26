from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, ContentType


class Command(BaseCommand):
    help = "Sets the required permission to add, change or delete a release"

    def add_arguments(self, parser):
        parser.add_argument("fas_group", type=str)

    def handle(self, *args, **options):
        fas_group = options["fas_group"]
        release_obj = ContentType.objects.get(app_label="releases")
        releases_permissions = list(release_obj.permission_set.all())
        group, created = Group.objects.get_or_create(name=fas_group)
        group.permissions.set(releases_permissions)

        self.stdout.write(
            self.style.SUCCESS(f"{fas_group} succesfully added to Releases permissions")
        )
