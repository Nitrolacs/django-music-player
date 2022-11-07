from main.form import AddCompositionForm, AddPlaylistForm
from django.shortcuts import render, redirect
from .models import Composition, PlayList

from main.utils import get_max_order


def homepage(request):
    playlist = PlayList.objects.all()
    composition = Composition.objects.all()
    composition_list = list(
        Composition.objects.all().values('title', 'artist', 'playlist__name', 'playlist__cover_image', 'time_length',
                                         'audio_file', 'cover_image'))
    return render(request, 'base.html', {
        'composition': composition,
        'composition_list': composition_list,
        'playlist': playlist,
    })


# Delete song
def delete_song(request, comp_id):
    song = Composition.objects.get(pk=comp_id)
    song.delete()
    return redirect("music_player:home_page")


# Delete playlist
def delete_pllst(request, pllst_id):
    playlist = PlayList.objects.get(pk=pllst_id)
    playlist.delete()
    return redirect("music_player:home_page")


def addSong(request):
    form = AddCompositionForm()
    playlist = PlayList.objects.all()
    if request.POST:
        form = AddCompositionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            playlist = form.cleaned_data.get('playlist')
            music_playlist = PlayList.objects.get_or_create(name=playlist)
            instance.playlist = music_playlist[0]
            instance.order = get_max_order()
            instance.save()
            return redirect("music_player:home_page")

    return render(request, 'addSong.html', {
        'form': form,
        'playlist': playlist,
    })


def addPlaylist(request):
    form = AddPlaylistForm()
    if request.POST:
        form = AddPlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("music_player:home_page")

    return render(request, 'addPlaylist.html', {
        'form': form
    })


def sort(request):
    comps_pks_order = request.POST.getlist('song_order')

    for idx, comp_pk in enumerate(comps_pks_order, start=1):
        tmpcomposition = Composition.objects.get(pk=comp_pk)
        tmpcomposition.order = idx
        tmpcomposition.save()
