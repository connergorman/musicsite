from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
    path("results/", views.ResultsView.as_view(), name='results'),
]
