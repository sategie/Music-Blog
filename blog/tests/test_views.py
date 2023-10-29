from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment, Profile, User
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('blogs')
        # Creating a staff user before making a request
        self.user = User.objects.create_user(
            username='superuser', password='superpassword', is_staff=True)
        # Logging in the newly created user
        self.client.login(username='superuser', password='superpassword')
        self.post1 = Post.objects.create(
            title='Test Post Title',
            slug='test-post',
            author=self.user,
            post_content='Test Content',
            status=1
        )
        self.detail_url = reverse('blog', args=[self.post1.slug])
        self.create_post_url = reverse('create_post')
        


    def test_post_list_GET(self):
        """
        Test that correct posts are retrieved using the right template
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_GET(self):
        """
        Test that the correct post is retrieved using the right template
        """
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    # def test_create_post_GET(self):
    #     """
    #     Test that the correct post is created using the right template
    #     """
    #     response = self.client.get(self.create_post_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_create.html')

    def test_create_post_GET(self):
        
        response = self.client.get(self.create_post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')






