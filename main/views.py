from django.shortcuts import render
from django.http import HttpResponse
from .models import Site, Podder, Resume

# Create your views here.
def homepage(request):
    return render(request=request, template_name="main/home.html", context={"sites":Site.objects.all})

def podder_page(request):
    return render(request, "main/podder.html", context={"podders":Podder.objects.all})

def resume(request):
    return render(request, "main/resume.html", context={"resumes":Resume.objects.all})