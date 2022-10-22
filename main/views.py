from django.shortcuts import render
from .models import Composition


def homepage(request):
    composition = Composition.objects.all()
    composition_list = list(Composition.objects.all().values())
    return render(request, 'base.html', {
        'composition': composition,
        'composition_list': composition_list
    })
