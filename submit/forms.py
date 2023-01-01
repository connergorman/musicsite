from django import forms
from django.utils.safestring import mark_safe

class ListenForm(forms.Form):
    artist = forms.CharField(label="Artist:", max_length=200)
    album = forms.CharField(label="Album:", max_length=200)
    track = forms.CharField(label="Track:", max_length=200)
    duration = forms.DurationField(label='Duration (hh:mm:ss):')
    date = forms.DateTimeField(label='Date Played',
                               widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YY HH:MM'}))


class ArtistForm(forms.Form):
    artist = forms.CharField(label='Artist:', max_length=200)
