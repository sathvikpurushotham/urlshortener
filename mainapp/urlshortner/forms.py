from django import forms
from .models import Shortner

class ShortenerForm(forms.ModelForm):
  original_url = forms.URLField(widget=forms.URLInput(attrs={ "placeholder": "Your URL to shorten"}))
  class Meta:
      model = Shortner
      fields = ('original_url',)