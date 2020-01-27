from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, ContentType


class Command(BaseCommand):
    help = "Sets the required permission to add, change or delete a resource"

    def add_arguments(self, parser):
        parser.add_argument("fas_group", type=str)
        parser.add_argument("resource", type=str, help="name of a resource, ie release")

    def handle(self, *args, **options):

        resource = ContentType.objects.get(app_label=options["resource"])
        permissions = list(resource.permission_set.all())
        group, created = Group.objects.get_or_create(name=options["fas_group"])
        for permission in permissions:
            group.permissions.add(permission)

        self.stdout.write(
            self.style.SUCCESS(
                f"{options['fas_group']} succesfully added to {options['resource']} permissions"
            )
        )
