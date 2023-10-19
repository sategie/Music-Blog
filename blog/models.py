from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
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
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    post_content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
    )

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

    def number_of_likes(self):
        """
        Returns the number of blog likes
        """
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug':self.slug}) 


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='blog_comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    comment_content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Displays the comments by the date of creation in ascending order
        """
        ordering = ['created_date']

    def __str__(self):
        """Returns comment content with name of comment creator"""
        return f'Comment {self.comment_content} by {self.author}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=70, default='')
    profile_pic = CloudinaryField('image', default='https://res.cloudinary.com/dvfxz4as6/image/upload/v1697302483/blank-profile-picture-973460_1280_skkwoi.png')
    bio = models.TextField()

    def __str__(self):
        return self.username