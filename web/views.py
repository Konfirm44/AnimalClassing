from django.shortcuts import render
from .models import Image
# Create your views here.

from django.http import HttpResponse


def index(request):
    # Pobranie pozycji z bazy danych
    images = Image.objects.all()
    # Stworzenie słownika przechowującego elementy
    # bazy danych pod zmienną news
    context = {'images': images}
    # Przełªanie wyrenderowanej strony wraz z dodanymi
    # elementami z bazy danych
    # elementy ze słownika context wykorzytywane
    # są w pliku news/index.html
    return render(request, 'index.html', context)