from time import perf_counter

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from todo_app.models import ToDoList, ToDoItem


class TestToDo(APITestCase):

    def setUp(self):
        self.to_do_list = ToDoList.objects.create(title='lol')
        self.to_do_item = ToDoItem.objects.create(
            title='title', description='description', todo_list=self.to_do_list
        )
        self.response_time = .1

    def test_list_list(self):
        start = perf_counter()
        response = self.client.get(reverse('list-lists'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_list_creation(self):
        data = {'title': 'title'}
        start = perf_counter()
        response = self.client.post(reverse('list-lists'), data=data)
        end = perf_counter()

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertLess(end-start, self.response_time)

    def test_get_detail(self):
        start = perf_counter()
        response = self.client.get(reverse('api-lists', kwargs={'pk': self.to_do_list.pk}))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_delete_list(self):
        start = perf_counter()
        response = self.client.delete(reverse('api-lists', kwargs={'pk': self.to_do_list.pk}))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertLess(end - start, self.response_time)

    def test_item_creation(self):
        data = dict(
            title='title', description='description'
        )

        start = perf_counter()
        response = self.client.post(reverse('create-item'), data=data)
        end = perf_counter()

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertLess(end - start, self.response_time)

    def test_item_partial_update(self):
        data = dict(
            title='title'
        )
        start = perf_counter()
        response = self.client.patch(reverse('api-item', kwargs={'pk': self.to_do_item.pk}), data=data)
        end = perf_counter()

        self.assertEqual(response.data['title'], 'title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_delete(self):
        start = perf_counter()
        response = self.client.delete(reverse('api-item', kwargs={'pk': self.to_do_item.pk}))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertLess(end - start, self.response_time)
