from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib import messages


def index(request):
    template = 'index.html'

    return render(request, template)


def post_list(request):
    template = 'post_list.html'
    posts = Post.objects.filter(status=1)
    context = {
        'blogs': posts
    }

    return render(request, template, context)


def post_detail(request, slug):
    """
    Function-based view which handles the display of a blog post as well as 
    the display/creation of comments associated with the selected post.
    """
    template = 'post_detail.html'
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.blog_comments.filter(
        approved=True).order_by('created_date')
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    commented = False

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            """
            Creates a new comment if the submitted form is valid.
            The new comment is linked to the current post with the author being 
            the currently logged in user.
            """
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(
                request, "Sent!")
            commented = True

    else:
        # If the request is not a Post request, an empty form is created
        comment_form = CommentForm()

    context = {
        'blog': post,
        'comments': comments,
        'commented': commented,
        'liked': liked,
        'comment_form': CommentForm()
    }

    return render(request, template, context)


# def like_post(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     post.likes.add(request.user)
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)
    
#     reversed_url = reverse('blog', args=[slug])
#     return HttpResponseRedirect(reversed_url)

def like_post(request, slug):
    """
    This function is used to manage the likes of a user on a blog post

    If the user clicks on the like button when they have already liked the post,
    the post is unliked, else the post is liked
    """
    post = get_object_or_404(Post, slug=slug)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    reversed_url = reverse('blog', args=[slug])
    return HttpResponseRedirect(reversed_url)
