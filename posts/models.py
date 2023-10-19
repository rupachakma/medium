from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=250)
    description = models.TextField()
    coverimage = models.ImageField(upload_to="blogimg",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Profileimage(models.Model):
    avatar = models.ImageField(upload_to="profileimg",blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)