from django import forms


class SearchTherapists(forms.Form):
    therapistName = forms.CharField(
        max_length=50,
        required=False,
    )
