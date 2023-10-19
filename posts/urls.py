
from django.urls import path

from posts import views


urlpatterns = [
    path('',views.home,name="homepage"),
    path('blog',views.blogpage,name="blog")
]
