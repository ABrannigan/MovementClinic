from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def homePage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"tutorials":BlogPost.objects.all})
