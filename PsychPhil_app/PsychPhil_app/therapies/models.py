from django.contrib.auth import get_user_model
from django.db import models

from PsychPhil_app.accounts.models import AppUser
from PsychPhil_app.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


class Therapy(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    NAME_MAX = 200
    DESCRIPTION_MAX = 1000

    name = models.CharField(
        max_length=NAME_MAX,
        blank=False,
        null=False,
    )

    description = models.CharField(
        max_length=DESCRIPTION_MAX,
        blank=False,
        null=False,
    )

    image = models.FileField(
        blank=True,
        null=True,
    )

    # therapists = models.Many(
    #     AppUser,
    #     blank=True
    # )

