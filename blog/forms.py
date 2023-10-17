from .models import Comment, Post
from django import forms

class CommentForm(forms.ModelForm):
    """
    Form for comments
    """
    class Meta:
        model = Comment
        fields = ('comment_content',)


class PostForm(forms.ModelForm):
    """
    Form for posts
    """
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author',
                  'featured_image', 'post_content', 'status']
