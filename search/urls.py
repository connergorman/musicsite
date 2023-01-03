from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
    path("results/", views.ResultsView, name='results'),
    path("results/albums/", views.showTracks, name='show tracks'),
]
