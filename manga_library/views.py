from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    return render(request=request, template_name="home.html")#, context={"sites":Site.objects.all})

def list_data(request):
    return render(request=request, template_name="list_authors.html", context={"authors": Author.objects.all().order_by('name')})

def list_series(request, author_pk):
    if author_pk == 0:
        context = Series.objects.all()
    else:
        context = Series.objects.filter(manga__author_id = author_pk).distinct()
    return render(request=request, template_name="list_series.html", context={"series": context.order_by('name')})

def list_manga(request, series_pk):
    context = Manga.objects.filter(series_id = series_pk)
    return render(request=request, template_name="list_manga.html", context={"manga": context.order_by('volume_number')})