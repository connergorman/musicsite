from django import forms
from django.utils.safestring import mark_safe
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ListenForm(forms.Form):
    artist = forms.CharField(label="Artist:", max_length=200)
    album = forms.CharField(label="Album:", max_length=200)
    track = forms.CharField(label="Track:", max_length=200)
    duration = forms.DurationField(label='Duration (hh:mm:ss):', 
                                   widget=forms.TextInput(attrs={'placeholder': 'MM:SS or HH:MM:SS'}))
    date = forms.DateTimeField(label='Date Played',
                               widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YY HH:MM'}),
                               required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'listen'

        self.helper.add_input(Submit('submit', 'Submit'))



class ArtistForm(forms.Form):
    artist = forms.CharField(label='Artist:', max_length=200)
