from django.db import models
from src.linked_list import LinkedList


class Composition(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500)
    playlist = models.ForeignKey('PlayList', on_delete=models.SET_NULL, null=True)
    time_length = models.DecimalField(blank=True, max_digits=20, decimal_places=2)
    audio_file = models.FileField(upload_to='musics/')
    cover_image = models.ImageField(upload_to='music_image/')

    def save(self, *args, **kwargs):
        if not self.time_length:
            # логика для получения длины музыкального трека
            pass
        return super().save(*args, **kwargs)


class PlayList(models.Model, LinkedList):
    pass
