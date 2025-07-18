from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    cctv = CCTV.objects.all()
    form = None
    if request.method == "POST":
        form = CCTVForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = CCTVForm()
    return render(request, "index.html", {"cctv":cctv, "form":form})
