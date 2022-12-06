from enum import Enum

from django.contrib.auth import models as auth_models
from django.db import models
from django.core import validators
from cloudinary import models as cloudinary_models

from PsychPhil_app.accounts.managers import AppUserManager
from PsychPhil_app.core.model_mixins import ChoicesEnumMixin
from PsychPhil_app.core.validators import validate_only_letters


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    Other = 'Other'


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_therapist = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    # See AppUserManager for explanation.
    objects = AppUserManager()


class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_SUMMARY = 30
    MAX_LEN_SUMMARY = 300

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        )
    )
# KINDA DONE I gotta make sure that these newly added are reflected in form and in edit profile. they should show up only if therapist and (optimally) be compulsary
    self_summary = models.TextField(
        max_length=MAX_LEN_SUMMARY,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LEN_SUMMARY),
        )
    )

    image = cloudinary_models.CloudinaryField(
        blank=True,
        null=False,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        blank=True,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="profile",
    )


# class AppUser(auth_models.AbstractUser):
#     MIN_LEN_FIRST_NAME = 2
#     MAX_LEN_FIRST_NAME = 30
#     MIN_LEN_LAST_NAME = 2
#     MAX_LEN_LAST_NAME = 30
#
#     first_name = models.CharField(
#         max_length=MAX_LEN_FIRST_NAME,
#         blank=True,
#         validators=(
#             validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
#             validate_only_letters,
#         )
#     )
#
#     last_name = models.CharField(
#         max_length=MAX_LEN_LAST_NAME,
#         blank=True,
#         validators=(
#             validators.MinLengthValidator(MIN_LEN_LAST_NAME),
#             validate_only_letters,
#         )
#     )
#
#     email = models.EmailField(
#         unique=True
#     )
#
#     gender = models.CharField(
#         choices=Gender.choices(),
#         max_length=Gender.max_len(),
#         blank=True,
#     )
#
#     is_therapist = models.BooleanField(
#         default=False,
#     )
