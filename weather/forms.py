from django import forms
from .models import City, Weather

class HomeForm(forms.ModelForm):
    search = forms.CharField()

    class Meta:
        model = City
        fields = ('lookup_city',)

