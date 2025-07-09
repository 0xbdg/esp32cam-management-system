from django import forms
from django.forms.widgets import *

from .models import *

class CCTVForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full bg-gray-800 border border-gray-700 px-3 py-2 text-sm focus:outline-none focus:border-blue-500", "placeholder":"e.g. Kitchen"}))
    cctv_url = forms.CharField(required=True, widget=URLInput(attrs={"class":"w-full bg-gray-800 border border-gray-700 px-3 py-2 text-sm focus:outline-none focus:border-blue-500", "placeholder":"http://192.168.x.x:81"}))

    class Meta:
        model = CCTV
        fields = ["name", "cctv_url"]

