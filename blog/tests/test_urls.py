from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import index, post_list, post_detail, like_post, create_post, modify_post, delete_post, user_profile, edit_profile

class TestUrls(SimpleTestCase):
    """
    Class for testing that urls resolve to the correct views
    """

    def test_home_success(self):
        """
        Test that the 'home' url resolves to the index view
        """
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, index)

    def test_create_post_success(self):
        """
        Test that the 'create_post' url resolves to the create_post view
        """
        url = reverse('create_post')
        print(resolve(url))
        self.assertEqual(resolve(url).func, create_post)

    def test_blogs_success(self):
        """
        Test that the 'blogs' url resolves to the post_list view
        """
        url = reverse('blogs')
        print(resolve(url))
        self.assertEqual(resolve(url).func, post_list)

    def test_blog_success(self):
        """
        Test that the 'blog' url resolves to the post_detail view
        The slug argument for blog (from urls.py) is passed into the url variable
        """
        url = reverse('blog', args=['test-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, post_detail)

    def test_modify_post_success(self):
        """
        Test that the 'modify_post' url resolves to the modify_post view
        The keyword arguments for modify_post are passed into the url variable
        """
        url = reverse('modify_post', kwargs={'slug': 'test-slug'})
        print(resolve(url))
        self.assertEqual(resolve(url).func, modify_post)

    def test_delete_post_success(self):
        """
        Test that the 'delete_post' url resolves to the delete_post view
        The keyword arguments for delete_post are passed into the url variable
        """
        url = reverse('delete_post', kwargs={'slug': 'test-slug'})
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_post)

    def test_like_post_success(self):
        """
        Test that the 'like_post' url resolves to the like_post view
        The slug argument for like_post is passed into the url variable
        """
        url = reverse('like_post', args=['test-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, like_post)

    def test_profile_success(self):
        """
        Test that the 'profile' url resolves to the user_profile view
        The username argument for profile is passed into the url variable
        """
        url = reverse('profile', args=['test-user'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, user_profile)

    def test_edit_profile_success(self):
        """
        Test that the 'edit_profile' url resolves to the edit_profile view
        The username argument for edit_profile is passed into the url variable
        """
        url = reverse('edit_profile', args=['test-user'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, edit_profile)
