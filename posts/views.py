from django.shortcuts import render

from posts.models import Blogpost

# Create your views here.
def home(request):
   return render(request, 'home.html')

def blogpage(request):
   posts = Blogpost.objects.all()
   
   return render(request,"blog.html",{"posts":posts})