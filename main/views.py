from django.shortcuts import render
from django.http import HttpResponse
from .models import Site
# Create your views here.
def homepage(request):
    return render(request=request, 
    template_name="main/home.html", 
    context={"sites":Site.objects.all})

def podder(request):
    return render(request=request, 
    template_name="main/podder.html", 
    context={"podder":Podder.objects.all})