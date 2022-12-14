from django import forms
from django.contrib.auth import get_user_model
from PsychPhil_app.therapies.models import Therapy

UserModel = get_user_model()


# These forms are not necessary.
class CreateTherapy(forms.ModelForm):
    class Meta:
        model = Therapy
        fields = ('name', 'summary', 'founder', 'url', 'description', 'image')


class EditTherapy(forms.ModelForm):
    class Meta:
        model = Therapy
        fields = ('name', 'summary', 'founder', 'url', 'description', 'image')
