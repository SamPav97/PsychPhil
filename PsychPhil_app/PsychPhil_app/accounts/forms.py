from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from PsychPhil_app.accounts.models import Profile, Gender

UserModel = get_user_model()


# I no longer really need this form as prof n user r connected with a signal. and I dont ask for first name etc on /
# on registration anyway
# Through the form I connect the profile and the user.
class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        required=False
    )
    last_name = forms.CharField(
        required=False
    )
    age = forms.IntegerField(
        required=False
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'age')


class EditForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True
    )
    last_name = forms.CharField(
        required=True
    )

    gender = forms.ChoiceField(
        choices=Gender.choices(),
        required=True
    )

    self_summary = forms.Textarea(
    )

    age = forms.IntegerField(
        required=True
    )
    image = forms.ImageField(
        required=False
    )

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'age', 'gender', 'self_summary', 'age', 'image', )

