from time import perf_counter

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from projects.models import Project


class TestProjects(APITestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title='title', description='description', technology='technology',
        )
        self.response_time = .1

    def test_list(self):
        start = perf_counter()
        response = self.client.get(reverse('projects-list'))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(end-start, self.response_time)

    def test_detail(self):
        start = perf_counter()
        response = self.client.get(reverse('api-projects', kwargs={'pk': self.project.pk}))
        end = perf_counter()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(end - start, self.response_time)