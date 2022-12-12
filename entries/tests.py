from time import perf_counter

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from entries.models import Entry
from my_users.models import MyUser


class TestEntries(APITestCase):

    def setUp(self):
        self.user = MyUser.objects.create(
            first_name='test', last_name='test',
            email='test@test.com', password='P123123123')
        self.entry = Entry.objects.create(title='test', content='test')

        self.client.force_authenticate(user=self.user)
        self.response_time = .1
        self.url = reverse('api-entry', kwargs={'pk': self.entry.pk})

    def test_get_list_entries(self):
        start = perf_counter()
        response = self.client.get(reverse('entry-list'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_get_detail_entry(self):
        start = perf_counter()
        response = self.client.get(self.url)
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_entry_creation(self):
        data = {
            'title': 'title',
            'content': 'content'
        }
        start = perf_counter()
        response = self.client.post(reverse('entry-list'), data=data)
        end = perf_counter()

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertLess(end - start, self.response_time)

    def test_partial_update(self):
        data = {
            'title': 'title',
        }
        start = perf_counter()
        response = self.client.patch(self.url, data=data)
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_delete(self):
        start = perf_counter()
        response = self.client.delete(self.url)
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

