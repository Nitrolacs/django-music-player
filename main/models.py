from django.db import models
from src.linked_list import LinkedList
from main.helpers import get_audio_length
from main.validators import validate_is_audio


class Composition(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    playlist = models.ForeignKey('PlayList', on_delete=models.SET_NULL, null=True, blank=True)
    time_length = models.DecimalField(blank=True, max_digits=20, decimal_places=2)
    audio_file = models.FileField(validators=[validate_is_audio])
    cover_image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.time_length:
            # логика для получения длины музыкального трека
            audio_length = get_audio_length(self.audio_file)
            self.time_length = audio_length
        return super().save(*args, **kwargs)


class PlayList(models.Model, LinkedList):
    pass
