from main.form import AddCompositionForm
from django.shortcuts import render, redirect
from .models import Composition, PlayList


def homepage(request):
    composition = Composition.objects.all()
    composition_list = list(Composition.objects.all().values())
    return render(request, 'base.html', {
        'composition': composition,
        'composition_list': composition_list
    })


def addSong(request):
    form = AddCompositionForm()
    if request.POST:
        form = AddCompositionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            playlist = form.cleaned_data.get('playlist')
            music_playlist = PlayList.objects.get_or_create(name=playlist)
            instance.playlist = music_playlist[0]
            instance.save()
            return redirect("music_player:home_page")

    return render(request, 'addSong.html', {
        'form': form
    })
