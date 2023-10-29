from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Post, Profile
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .forms import CommentForm, PostForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.db import IntegrityError



def index(request):
    """
    Landing page
    """
    template = 'index.html'

    return render(request, template)


def post_list(request):
    """
    Shows the list of posts with 5 posts per page
    """
    template = 'post_list.html'
    posts = Post.objects.filter(status=1)
    # Pagination - 6 posts per page
    paginator = Paginator(posts, 6)
    # Getting the page number from the GET request parameters
    page_number = request.GET.get('page')
    # Getting the Page object for the given page number
    page_obj = paginator.get_page(page_number)
    context = {
        'blogs': page_obj
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

@login_required
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


@login_required
@staff_member_required
def create_post(request):
    template = 'post_create.html'
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # Capitalize the first letter in each word in the title
            post.title = post.title.title()

            post.slug = slugify(post.title)
            # Set author to the currently logged in user
            post.author = request.user
            
            try:
                post.save()
            # Handle cases where a slug already exists for a given title
            except IntegrityError:
                messages.error(
                    request, 'A post with the same title or slug already exists.')
                context = {
                    'form': form
                }
                return render(request, template, context)

            reversed_url = reverse('blogs')
            return HttpResponseRedirect(reversed_url)
            
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
@staff_member_required
def modify_post(request, slug):
    """
    The function does the following:
    - gets the post instance related to the slug
    - checks if request is POST
    - saves the form's data without commiting to the database
    - modifies the slug depending on the title of the post
    - saves the post to the database afterwards
    - after saving to the database, the user is redirected to the specific 
      blog's page
    - if it is not a POST request, the initial form is displayed
    """
    template = 'post_modify.html'
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # Capitalize the first letter in each word in the title
            post.title = post.title.title()

            post.slug = slugify(post.title)
            # Sets author to the currently logged in user
            post.author = request.user

            try:
                post.save()
            # Handle cases where a slug already exists for a given title
            except IntegrityError:
                messages.error(
                    request, 'A post with the same title or slug already exists.')
                context = {
                    'form': form
                }
                return render(request, template, context)

            reversed_url = reverse('blog', args=[slug])
            return HttpResponseRedirect(reversed_url)
    else:
        form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
@staff_member_required
def delete_post(request, slug):
    """
    The function does the following:
    - gets the post instance related to the slug
    - deletes the post
    - after deleting the post, the user is redirected to the post list page
    """
    template = 'post_delete.html'
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post has been deleted successfully.')
        reversed_url = reverse('blogs')
        return HttpResponseRedirect(reversed_url)
    else:
        context = {
            'post': post
        }
        return render(request, template, context)


@login_required
@staff_member_required
def user_profile(request, username):
    template = 'profile.html'
    profile = get_object_or_404(Profile, user__username=username)
    blog_posts = Post.objects.filter(author=request.user)
    context = {
        'profile': profile,
        'blog_posts': blog_posts
    }
    return render(request, template, context)


@login_required
@staff_member_required
def edit_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            reversed_url = reverse('profile', args=[username])
            return HttpResponseRedirect(reversed_url)
    else:
        form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)
