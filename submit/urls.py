from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('album/', views.submit_album, name='submit album'),
        path('track/', views.submit_track, name='submit track'),
        path('listen/', views.submit_listen, name='listen')
]
