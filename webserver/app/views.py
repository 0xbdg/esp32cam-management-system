from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == "POST":
        pass
    cctv = CCTV.objects.all()
    return render(request, "index.html", {"cctv":cctv})
