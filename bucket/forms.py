from django import forms

from .models import Download

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Download
        fields = ('url',)

