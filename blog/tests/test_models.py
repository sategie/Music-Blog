from django.test import TestCase
from blog.models import Post, Comment, Profile
from django.contrib.auth.models import User

class TestModels(TestCase):
    """
    Test models in blog app
    """
    def setUp(self):
        """
        Set up test environment
        """
        # Create a User instance
        self.user = User.objects.create(username='superuser', password='superpassword')
        # Create a Post instance
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            post_content='This is a test post'
        )
        # Create a Comment instance
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            comment_content='This is a test comment'
        )
        # Create a Profile instance
        self.profile = Profile.objects.create(
            user=self.user,
            full_name='Test User',
            username='superuser'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, 'Test Post')

    def test_comment_creation(self):
        self.assertEqual(self.comment.author, self.user)
        self.assertEqual(self.comment.comment_content,
                         'This is a test comment')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.username, 'superuser')

