from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import PointSet

class PointSetAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('pointset-list')

    def test_create_point_set(self):
        data = {'points': '2,2;-1,30;20,11;4,5'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PointSet.objects.count(), 1)
        point_set = PointSet.objects.first()
        self.assertEqual(point_set.points, '2,2;-1,30;20,11;4,5')
        self.assertEqual(point_set.closest_points, '2,2;4,5')

    def test_create_point_set_invalid_input(self):
        data = {'points': '2,2;-1,30'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PointSet.objects.count(), 0)

    def test_get_point_set(self):
        point_set = PointSet.objects.create(points='2,2;-1,30;20,11;4,5', closest_points='2,2;4,5')
        response = self.client.get(reverse('pointset-list', args=[point_set.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['points'], '2,2;-1,30;20,11;4,5')
        self.assertEqual(response.data['closest_points'], '2,2;4,5')

    def test_get_point_set_not_found(self):
        response = self.client.get(reverse('pointset-list', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
