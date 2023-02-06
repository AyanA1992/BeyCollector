from django.forms import ModelForm
from .models import Shows


"""
Django's ModelFrom class is designed
to create an HTML5 from from a model
"""

class ShowsForm(ModelForm):
    class Meta:
        model = Shows
        fields = ('date', 'sets')

