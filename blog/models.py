from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    """
    A Post class which subclasses from django.db.models.Model

    Takes in a variety of attributes which make up the Database columns for 
    the Post entity
    """
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='modified_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    post_content = models.TextField()
    status = models.IntegerField()
