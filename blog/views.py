from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm


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
    commented = False

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            commented = True

    else:
        comment_form = CommentForm()

    context = {
        'blog': post,
        'comments': comments,
        'commented': commented,
        'comment_form': CommentForm()
    }

    return render(request, template, context)
