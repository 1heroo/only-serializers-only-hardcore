from time import perf_counter

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestPycats(APITestCase):

    def test_only_endpoint(self):

        start = perf_counter()
        response = self.client.get(reverse('podcasts'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(end-start, .1)