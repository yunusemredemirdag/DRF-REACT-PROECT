from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class PostTests(APITestCase):
    
    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.test_user1 = User.objects.create(username='test_user1', password='123456789')
        data = {
            "title": "new",
            "author": 1,
            "excerpt": "new",
            "content": "new"
        }
        url = reverse('blog_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    
    def test_post_update(self):
        
        client = APIClient()
        
        self.test_category = Category.objects.create(name='django')
        self.test_user1 = User.objects.create(username='test_user1', password='123456789')
        self.test_user2 = User.objects.create(username='test_user2', password='123456789')
        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published'
        )
        
        client.login(username=self.test_user1.username, password='123456789')
        
        url = reverse(('blog_api:detailcreate'), kwargs={'pk': 1})
        
        response = client.put(url, {
            "title": "New",
            "author": 1,
            "excerpt": "New",
            "content": "New",
            "status": "published"
        }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
