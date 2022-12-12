from time import perf_counter

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestCore(APITestCase):

    def test_request_endpoint(self):
        start = perf_counter()
        response = self.client.get(reverse('request-info'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(end-start, .1)

    def test_user_endpoint(self):
        start = perf_counter()
        response = self.client.get(reverse('user-info'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(end - start, .1)