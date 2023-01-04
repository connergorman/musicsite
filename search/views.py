from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# from .forms import SearchForm
from submit.models import Album, Artist, Track

# Create your views here.
def index(request):
    return HttpResponse("This is index")


class SearchView(TemplateView):
    template_name = "search/search.html"

def testView(request):
    return render(request, "search/test.html")


def ResultsView(request):
    template_name = 'search/results.html'
    model = Album
    object_list = {}
    if request.method == 'GET': 
        query = request.GET.get("q")
        object_list = Album.objects.filter(
            Q(artist__name__icontains=query) | Q(album_name__icontains=query)
        )
        context = {'albums': object_list}
        return render(request, template_name, context=context)
    else:
        album = request.POST.get('a')
        context = { 'album' : album.album_name, 'artist' : album.artist.name }
        return render(request, 'results.html', context)
       
def showTracks(request):
    template_name = 'search/albums.html'
    if request.method == 'POST':
        choices = list(request.POST.items())[1:]
        albums = []
        for a,b in choices:
            albums.append(Album.objects.filter(Q(artist__name__icontains=b) & Q(album_name__icontains=a)).first())


        context = { 'albums' : albums }
        return render(request, template_name, context)
        




#def search(request):
#    template_name = "search.html"
#
#
#def results(request):
#    template_view = "results.html"
