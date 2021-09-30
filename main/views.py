from django.shortcuts import render
from django.http import HttpResponse
from .models import Site, Podder, Resume, Blog, Podcast
from django.views.generic import ListView, DetailView


class BlogPost(DetailView):
    model = Blog
    template_name = 'main/blog_post.html'

class BlogList(ListView):
    model = Blog
    template_name = 'main/blog_list.html'

# Create your views here.
def homepage(request):
    return render(request=request, template_name="main/home.html", context={"sites":Site.objects.all})

def podder_page(request):
    return render(request, "main/podder.html", context={"podders":Podder.objects.all})

def resume(request):
    return render(request, "main/resume.html", context={"resumes":Resume.objects.all})

def podcast_list(request):
    return render(request, "main/podcast_list.html", context={"podcasts":Podcast.objects.all})

'''
def blog_post(request, id):
#    post = Blog.objects.get(id=id)
#    context = {'post':post}
    return render(request, 'main/blog_post.html', {})
'''