from django.shortcuts import render
from django.http import HttpResponse
# from .forms import SearchForm 

# Create your views here.
def index(request):
    return HttpResponse("This is index")
