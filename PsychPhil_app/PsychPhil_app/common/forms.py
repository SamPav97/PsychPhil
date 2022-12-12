
from django import forms


class SearchPhotosTherapists(forms.Form):
    therapistName = forms.CharField(
        max_length=50,
        required=False,
    )
