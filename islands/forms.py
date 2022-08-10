from socket import fromshare
from django import forms
from .models import Island


class IslandForm(forms.ModelForm):
    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}))

    class Meta:
        model = Island
        fields = ["name", "photos"]
