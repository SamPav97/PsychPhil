
from django.contrib.auth import get_user_model
from django.db import models
from cloudinary import models as cloudinary_models

UserModel = get_user_model()


class TherapistCand(models.Model):
    MAX_MOTIVATION = 5000
    motivation = models.TextField(
        max_length=MAX_MOTIVATION,
        null=False,
        blank=False,
    )

    cv = cloudinary_models.CloudinaryField(
        blank=False,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )
