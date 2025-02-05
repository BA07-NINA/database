from typing import Self

from django.core.management import call_command
from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    def handle(self: Self, **options) -> None:
        if User.objects.all().first() is None:
            call_command("loaddata", "users.json")
