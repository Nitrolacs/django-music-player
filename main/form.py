from django import forms
from .models import Composition


class AddCompositionForm(forms.ModelForm):
    playlist = forms.CharField(max_length=500, required=True)

    class Meta:
        model = Composition
        fields = ["title", "artist", "audio_file", "cover_image"]
