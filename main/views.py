from main.form import AddComposition
from django.shortcuts import render
from .models import Composition


def homepage(request):
    composition = Composition.objects.all()
    composition_list = list(Composition.objects.all().values())
    return render(request, 'base.html', {
        'composition': composition,
        'composition_list': composition_list
    })

def addSong(request):
    form = AddComposition()
    return render(request, 'addSong.html', {
        'form': form
    })