from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):

    category_name = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("blog-categories")
    

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    book = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
