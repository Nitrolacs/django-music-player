from django.urls import path
from . import views

app_name = "music_player"

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('add_song/', views.addSong, name="add_song")
]
