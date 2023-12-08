"""Forms of the project."""

# Create your forms here.

from django import forms
from django.forms import ModelForm
from .models import *

class ThingForm(forms.Form):
    """Form for creating a Thing."""
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField()
