from django import forms
from django.forms.widgets import *

from .models import *

class CCTVForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=TextInput(attrs={"class":""}))
    cctv_url = forms.CharField(required=True, widget=URLInput(attrs={"class":""}))

    class Meta:
        model = CCTV
        fields = ["name", "cctv_url"]

