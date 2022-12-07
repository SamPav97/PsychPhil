from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from PsychPhil_app.accounts.models import Profile

UserModel = get_user_model()


# Make signal every time a post request is made, save a profile with according primary key.
# In this app saves are only made for new profs. This signal should not activate from signals coming
# from other apps.
@receiver(signals.post_save, sender=UserModel)
def create_employee_on_user_created(instance, created, *args, **kwargs):
    if not created:
        return
    Profile.objects.create(
        user_id=instance.pk,
    )


# Delete prof when appuser gets deleted
@receiver(signals.pre_delete, sender=UserModel)
def delete_profile_when_account_deleted(instance, **kwargs):
    Profile.objects.get(
        user_id=instance.pk,
    ).delete()
