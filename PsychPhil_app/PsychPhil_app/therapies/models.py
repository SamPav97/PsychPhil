from django.contrib.auth import get_user_model
from cloudinary import models as cloudinary_models
from django.db import models
from PsychPhil_app.accounts.models import AppUser
from PsychPhil_app.core.model_mixins import StrFromFieldsMixin

UserModel = get_user_model()


# I use this mixin to create the string method of the class.
class Therapy(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')
    NAME_MAX = 200
    SUMMARY_MAX = 300
    DESCRIPTION_MAX = 1000

    name = models.CharField(
        max_length=NAME_MAX,
        blank=False,
        null=False,
    )

    summary = models.CharField(
        max_length=SUMMARY_MAX,
        blank=False,
        null=False,
    )

    founder = models.CharField(
        max_length=NAME_MAX,
        blank=False,
        null=False,
    )

    url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX,
        blank=False,
        null=False,
    )

    image = cloudinary_models.CloudinaryField(
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        blank=True,
        on_delete=models.CASCADE,
    )

    therapists = models.ManyToManyField(
        AppUser,
        blank=True,
        related_name="therapists",
    )

