from django.contrib import admin

from posts.models import *

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Profileimage)