from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment, Profile
from django.contrib.auth.models import User


class TestViews(TestCase):
    """
    Class for testing views
    """

    def setUp(self):
        """
        Set up test environment
        """
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
        self.index_url = reverse('home')
        self.detail_url = reverse('blog', args=[self.post1.slug])
        self.create_post_url = reverse('create_post')
        self.modify_post_url = reverse(
            'modify_post', kwargs={'slug': self.post1.slug})
        self.delete_post_url = reverse(
            'delete_post', kwargs={'slug': self.post1.slug})
        # self.profile_url = reverse(
        #     'profile', args=[self.user.username])
        self.like_post_url = reverse('like_post', args=[self.post1.slug])

    def test_index_GET(self):
        """
        Test that index page is correctly retrieved using the right template
        """
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_post_list_GET(self):
        """
        Test that post_list is correctly retrieved using the right template
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_GET(self):
        """
        Test that post_detail is correctly retrieved using the right template
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_create_post_GET(self):
        """
        Test that create_post is correctly retrieved using the right template
        """
        response = self.client.get(self.create_post_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_create.html')

    def test_modify_post_GET(self):
        """
        Test that modify_post is correctly retrieved using the right template
        """
        response = self.client.get(self.modify_post_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_modify.html')

    def test_delete_post_GET(self):
        """
        Test that delete_post is correctly retrieved using the right template
        """
        response = self.client.get(self.delete_post_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_delete.html')

    def test_like_post_POST(self):
        """
        Test if like increases by 1 when like_post a user likes a post
        Test if the like is removed if the user likes the post again
        """

        initial_likes = self.post1.likes.count()

        # Should add one like
        response = self.client.get(self.like_post_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post1.likes.count(), initial_likes + 1)
        # Should remove the like added in the previous step
        response = self.client.get(self.like_post_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post1.likes.count(), initial_likes)

    def test_create_post_POST(self):
        """
        Test that the create_post view can create a new post
        """
        response = self.client.post(
            self.create_post_url, {
                'title': 'New Post Title',
                'slug': 'new-post',
                'author': self.user.id,
                'post_content': 'New Post Content',
                'status': 1
            })
        # fetches the most recently created post
        new_post = Post.objects.order_by('-post_id')[0]
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_post.title, 'New Post Title')
        new_post.delete()

    def test_post_comment_POST(self):
        """
        Test that the post_detail view can create a new comment from the Post page
        """
        response = self.client.post(self.detail_url, {
            'comment_content': 'New Comment Content'
        })
        new_comment = Comment.objects.order_by('-id')[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_comment.comment_content, 'New Comment Content')
        new_comment.delete()

    def test_post_invalid_comment_POST(self):
        """
        Test that the post_detail view does not create a new comment on invalid POST data
        """
        response = self.client.post(self.detail_url, {
            'comment_content': '' 
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['comment_form'].is_valid())

    

    







