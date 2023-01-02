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


class ResultsView(ListView):
    template_name = 'search/results.html'
    model = Album
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Album.objects.filter(
            Q(artist__name__icontains=query) | Q(album_name__icontains=query)
        )
        return object_list


#def search(request):
#    template_name = "search.html"
#
#
#def results(request):
#    template_view = "results.html"
