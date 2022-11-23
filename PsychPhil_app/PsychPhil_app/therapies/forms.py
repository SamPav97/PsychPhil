from django import forms
from django.contrib.auth import get_user_model

from PsychPhil_app.therapies.models import Therapy

UserModel = get_user_model()


class CreateTherapy(forms.ModelForm):
    class Meta:
        model = Therapy
        fields = '__all__'
