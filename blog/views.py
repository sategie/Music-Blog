from django.shortcuts import render, get_object_or_404
from .models import Post


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
    template = 'post_detail.html'
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.blog_comments.filter(
        approved=True).order_by('-created_date')
    context = {
        'blog': post,
        'comments': comments,
    }

    return render(request, template, context)
