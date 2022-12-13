from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from PsychPhil_app import settings
from PsychPhil_app.therapistCandidate.models import TherapistCand

UserModel = get_user_model()


# Send email when a user applies to become therapist.
@receiver(signal=post_save, sender=TherapistCand)
def send_email_on_successful_application_for_therapist(instance, created, **kwargs):

    user = UserModel.objects.all() \
        .filter(pk=instance.user_id) \
        .get()

    if not created:
        return

    email_content = render_to_string('email_templates/successfully_applied_for_therapist.html', {
        'user': user,
    })
    send_mail(
        subject='You applied for therapist at PsychPhil!',
        message=strip_tags(email_content),
        html_message=email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(user.email,),
    )
