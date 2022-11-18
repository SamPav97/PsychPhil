from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms

from PsychPhil_app.accounts.models import Profile

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

    # I now save with a signal
    # # save with data for profile
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     profile = Profile(
    #         first_name=self.cleaned_data['first_name'],
    #         last_name=self.cleaned_data['last_name'],
    #         age=self.cleaned_data['age'],
    #         user=user,
    #     )
    #     if commit:
    #         profile.save()
    #
    #     return user

