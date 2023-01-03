from django import forms

class AlbumSelectForm(forms.Form):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, choices):
        self.choices = choices
    #choices = self.choices
    #choice_field = forms.MultipleChoiceField(choices=choices)
    


