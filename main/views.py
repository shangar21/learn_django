from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse("This is html in <strong>Python</strong>. <button>this is a button</button>")
