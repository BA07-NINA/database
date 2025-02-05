from typing import Self

from django.apps import AppConfig as DjangoAppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(DjangoAppConfig):
    name = "pam"
    verbose_name = _("PAM")

    def ready(self: Self) -> None:
        try:
            import pam.signals  # noqa: F401
        except ImportError:
            pass
