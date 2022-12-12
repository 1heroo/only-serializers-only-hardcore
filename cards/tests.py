from time import perf_counter

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from blog.models import Post, Category
from cards.models import Card


class TestCARDAPIView(APITestCase):

    def setUp(self):
        self.card = Card.objects.create(
            question='question', answer='answer',
            box=1
        )
        self.response_time = .1

    def test_get_list_card(self):
        start = perf_counter()
        response = self.client.get(reverse('card-list'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_card_creation(self):
        data = dict(
            question='question',
            answer='answer',
            box=1
        )
        start = perf_counter()
        response = self.client.post(reverse('card-list'), data=data)
        end = perf_counter()

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertLess(end - start, self.response_time)

    def test_partial_update(self):
        data = dict(
            question='question',
            answer='answer',
            box=1
        )
        start = perf_counter()
        response = self.client.patch(reverse('api-cards', kwargs={'pk': self.card.pk}), data=data)
        end = perf_counter()

        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)

    def test_boxes(self):
        start = perf_counter()
        response = self.client.get(reverse('api-box', kwargs={'box_id': self.card.box}))
        end = perf_counter()

        self.assertNotEqual(response.data, False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLess(end - start, self.response_time)