from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """
    A Post class which subclasses from django.db.models.Model

    Takes in a variety of attributes which make up the Database columns for
    the Post entity
    """
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    post_content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """
        Displays the posts by the date of creation in descending order
        """
        ordering = ['-created_date']

    def __str__(self):
        """
        Built in Django function which returns a string representation
        of an object
        """
        return self.title

    def blog_snippet(self):
        """
        Returns a predefined amount of characters on the blogs page for each
        blog and adds trailing dots to indicate a preview
        """
        return self.post_content[:100] + '...'
