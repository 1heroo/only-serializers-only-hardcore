from time import perf_counter

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from blog.models import Post, Category


class TestBlog(APITestCase):

    def setUp(self):
        self.blog = Post.objects.create(
            title='test', body='test',
        )
        self.response_time = .1

    def test_list_posts(self):
        start = perf_counter()
        response = self.client.get(reverse('list-posts'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end-start, self.response_time)

    def test_list_categories(self):
        start = perf_counter()
        response = self.client.get(reverse('categories-list'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_comment_creation(self):
        data = {
            'author': 'Author',
            'body': 'test',
            'post': self.blog.pk
        }
        start = perf_counter()
        response = self.client.post(reverse('comments'), data=data)
        end = perf_counter()

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertLess(end - start, self.response_time)

    def test_post_detail_get(self):

        start = perf_counter()
        response = self.client.get(reverse('api-posts', kwargs={'pk': self.blog.pk}))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)
