from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class TherapistCand(models.Model):
    MAX_MOTIVATION = 5000
    motivation = models.CharField(
        max_length=MAX_MOTIVATION,
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
