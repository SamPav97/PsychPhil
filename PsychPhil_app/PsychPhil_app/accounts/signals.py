from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from PsychPhil_app import settings
from PsychPhil_app.accounts.models import Profile

UserModel = get_user_model()


# Make signal every time a post request is made, save a profile with according primary key.
@receiver(signals.post_save, sender=UserModel)
def create_employee_on_user_created(instance, created, *args, **kwargs):
    if not created:
        return
    Profile.objects.create(
        user_id=instance.pk,
    )


# Delete prof when AppUser gets deleted.
@receiver(signals.pre_delete, sender=UserModel)
def delete_profile_when_account_deleted(instance, **kwargs):
    Profile.objects.get(
        user_id=instance.pk,
    ).delete()


# Email user upon account creation.
@receiver(signal=post_save, sender=UserModel)
def send_email_on_successful_sign_up(instance, created, **kwargs):
    if not created:
        return

    email_content = render_to_string('email_templates/successful_sign_up.html', {
        'user': instance,
    })

    send_mail(
        subject='Welcome to PsychPhil!',
        message=strip_tags(email_content),
        html_message=email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(instance.email,),
    )
