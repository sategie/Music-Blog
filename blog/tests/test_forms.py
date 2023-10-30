from django.test import TestCase
from blog.forms import CommentForm, PostForm, ProfileForm
from blog.models import Post, Profile
from django.contrib.auth.models import User


class TestForms(TestCase):
    """
    Test class for testing forms
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.user = User.objects.create_user('testuser', 'testpassword')
        self.comment_form = CommentForm()
        self.post_form = PostForm()
        self.profile_form = ProfileForm()

    def test_comment_form_has_fields(self):
        """
        Test that fields in comment form exist and are in the expected order
        """
        expected = ['comment_content']
        actual = list(self.comment_form.fields)
        self.assertSequenceEqual(expected, actual)

    def test_post_form_has_fields(self):
        """
        Test that fields in post form exist and are in the expected order
        """
        expected = ['title', 'author',
                    'featured_image', 'post_content', 'status']
        actual = list(self.post_form.fields)
        self.assertSequenceEqual(expected, actual)

    def test_profile_form_has_fields(self):
        """
        Test that fields in profile form exist and are in the expected order
        """
        expected = ['full_name', 'bio']
        actual = list(self.profile_form.fields)
        self.assertSequenceEqual(expected, actual)