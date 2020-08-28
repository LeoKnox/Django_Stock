from django import forms

class RoomForm(forms.Form):
    name = forms.CharField(max_length = 50)