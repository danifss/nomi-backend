from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

        class Meta:
            unique_together = ('email',)
