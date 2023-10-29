from django.test import TestCase
from blog.forms import CommentForm, PostForm, ProfileForm
from blog.models import Post, Profile
from django.contrib.auth.models import User



class TestCommentForm(TestCase):
    """
    Test that fields on comment form exist and are in the expected order
    """
    def setUp(self):
        self.form = CommentForm()

    def test_form_has_fields(self):
        expected = ['comment_content']
        actual = list(self.form.fields)
        self.assertSequenceEqual(expected, actual)


class TestPostForm(TestCase):
    """
    Test that fields on post form exist and are in the expected order
    """
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'testpassword')
        self.form = PostForm()

    def test_form_has_fields(self):
        expected = ['title', 'author',
                    'featured_image', 'post_content', 'status']
        actual = list(self.form.fields)
        self.assertSequenceEqual(expected, actual)


class TestProfileForm(TestCase):
    """
    Test that fields on profile form exist and are in the expected order
    """
    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'testpassword')
        self.form = ProfileForm()

    def test_form_has_fields(self):
        expected = ['full_name', 'bio']
        actual = list(self.form.fields)
        self.assertSequenceEqual(expected, actual)

