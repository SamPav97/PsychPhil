from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ClientContact(models.Model):
    MAX_SUBJECT = 300

    subject = models.CharField(
        max_length=MAX_SUBJECT,
        blank=False,
        null=False,
    )

    content = models.TextField(
        blank=False,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )


from django.db import models

# Create your models here.
