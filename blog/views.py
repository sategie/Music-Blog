from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    template = 'index.html'

    return render(request, template)


def post_list(request):
    template = 'post_list.html'
    posts = Post.objects.all()
    context = {
        'blogs': posts
    }

    return render(request, template, context)


def post_detail(request, post_id):
    template = 'post_detail.html'
    post = get_object_or_404(Post, post_id=post_id)
    context = {
        'blog': post
    }

    return render(request, template, context)
