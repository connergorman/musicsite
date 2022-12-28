from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ListenForm
from .models import Listen
from .submit_to_db import submit_track

# Create your views here.
def index(request):
    return HttpResponse("Hello, World") 

def submit_album(request):

    return HttpResponse("You are submitting an album")


def listen(request):
    if request.method == 'POST':
        form = ListenForm(request.POST)
        if form.is_valid():
            submit_track(form.cleaned_data)
            return HttpResponse(str(form.cleaned_data))
    else:
        form = ListenForm()
    return render(request, 'listen.html', {'form': form})
