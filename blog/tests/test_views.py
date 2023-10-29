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
        # create a profile for the above user

        # self.profile1 = Profile.objects.create(user=self.user)

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
        self.modify_post_url = reverse(
            'modify_post', kwargs={'slug': self.post1.slug})
        self.delete_post_url = reverse(
            'delete_post', kwargs={'slug': self.post1.slug})
        # self.profile_url = reverse(
        #     'profile', args=[self.user.username])
        self.like_post_url = reverse('like_post', args=[self.post1.slug])

    

    def test_post_list_GET(self):
        """
        Test that post_list is correctly retrieved using the right template
        """
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_GET(self):
        """
        Test that post_detail is correctly retrieved using the right template
        """
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')


    def test_create_post_GET(self):
        """
        Test that create_post is correctly retrieved using the right template
        """
        
        response = self.client.get(self.create_post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')

    def test_modify_post_GET(self):
        """
        Test that modify_post is correctly retrieved using the right template
        """
        response = self.client.get(self.modify_post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_modify.html')

    def test_delete_post_GET(self):
        """
        Test that delete_post is correctly retrieved using the right template
        """
        response = self.client.get(self.delete_post_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_delete.html')


    def test_like_post_GET(self):
        """
        Test if like increases by 1 when like_post is retrieved
        Test if the like is removed if the another such request is made
        """

        initial_likes = self.post1.likes.count()

        # Should add one like
        response = self.client.get(self.like_post_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.post1.likes.count(), initial_likes + 1)
        # Should remove the like added in the previous step
        response = self.client.get(self.like_post_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.post1.likes.count(), initial_likes)


    

    







