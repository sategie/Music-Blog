from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    template = 'index.html'

    return render(request, template)


def post_list(request):
    template = 'post_list.html'
    posts = Post.objects.all()
    context = {
        'page_title': 'Blogs',
        'blogs': posts
    }

    return render(request, template, context)
