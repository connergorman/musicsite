from django import forms


class ListenForm(forms.Form):
    artist = forms.CharField(label="Artist:", max_length=200)
    album = forms.CharField(label="Album:", max_length=200)
    track = forms.CharField(label="Track:", max_length=200)
    duration = forms.DurationField(label='Duration (hh:mm:ss):') 
    date = forms.DateTimeField(label='Date Played (MM/DD/YY HH:MM):')
