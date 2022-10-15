from django.shortcuts import render
from .models import Composition


def homepage(request):
    composition = Composition.objects.all()
    return render(request, 'base.html', {
        'composition':composition
    })
