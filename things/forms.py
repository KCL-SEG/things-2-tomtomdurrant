"""Forms of the project."""

# Create your forms here.

from django import forms
from django.forms import ModelForm
from .models import *

class ThingForm(forms.Form):
    """Form for creating a Thing."""
    name = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(min_value=0, max_value=50)
