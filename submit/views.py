from django.shortcuts import render
from django.http import HttpResponse
from .forms import ListenForm
from .forms import ArtistForm
# from .models import Listen
from .submit_to_db import add_listen, add_artist


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def submit_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            add_artist(form.cleaned_data)
            return HttpResponse(str(form.cleaned_data))


def submit_album(request):

    return HttpResponse("You are submitting an album")


def submit_track(request):
    return HttpResponse("You are submitting a track")


def submit_listen(request):
    if request.method == 'POST':
        form = ListenForm(request.POST)
        if form.is_valid():
            add_listen(form.cleaned_data)
            return HttpResponse(str(form.cleaned_data))
    else:
        form = ListenForm()
    return render(request, 'listen.html', {'form': form})
