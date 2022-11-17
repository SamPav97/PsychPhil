from enum import Enum

from django.contrib.auth import models as auth_models
from django.db import models
from django.core import validators

from PsychPhil_app.core.model_mixins import ChoicesEnumMixin
from PsychPhil_app.core.validators import validate_only_letters


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    Other = 'Other'


class AppUser(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

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

    email = models.EmailField(
        unique=True
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        blank=True,
    )

    is_therapist = models.BooleanField(
        default=False,
    )
