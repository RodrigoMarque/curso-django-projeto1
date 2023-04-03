from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Rodrigo Marques'
    })


def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return render(request, 'me-apague/temp.html')
