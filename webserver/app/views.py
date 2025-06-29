from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    cctv = CCTV.objects.all()
    return render(request, "index.html")
