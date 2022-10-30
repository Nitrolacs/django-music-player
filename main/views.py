from main.form import AddCompositionForm
from django.shortcuts import render, redirect
from .models import Composition, PlayList

from django.contrib import messages


def homepage(request):
    composition = Composition.objects.all()
    composition_list = list(Composition.objects.all().values())
    return render(request, 'base.html', {
        'composition': composition,
        'composition_list': composition_list
    })


# Delete an Event
def delete_song(request, comp_id):
    song = Composition.objects.get(pk=comp_id)
    song.delete()
    return redirect("music_player:home_page")


def addSong(request):
    form = AddCompositionForm()
    if request.POST:
        form = AddCompositionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            playlist = form.cleaned_data.get('playlist')
            music_playlist = PlayList.objects.filter(name=playlist).exists()
            if not music_playlist:
                print('There is no such playlist! First create it.')
                messages.warning(request, 'There is no such playlist! First create it.')
            else:
                music_playlist = PlayList.objects.get_or_create(name=playlist)
                instance.playlist = music_playlist[0]
                instance.save()
                return redirect("music_player:home_page")

    return render(request, 'addSong.html', {
        'form': form
    })
