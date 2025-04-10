from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import AlumniFace
from ..serializers.alumni_faces_serializer import AlumniFaceSerializer


class AlumniFacesListViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.face1 = AlumniFace.objects.create(
            image_path="faces/face1.jpg",
            user=self.user
        )
        self.face2 = AlumniFace.objects.create(
            image_path="faces/face2.jpg",
            user=self.user
        )
        self.url = reverse('alumni_faces')

    def test_get_all_faces(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 2)

        faces = AlumniFace.objects.all()
        serializer = AlumniFaceSerializer(faces, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_response_structure(self):
        response = self.client.get(self.url)
        first_item = response.data[0]

        self.assertIn('id', first_item)
        self.assertIn('image_path', first_item)

        self.assertIsInstance(first_item['id'], int)
        self.assertIsInstance(first_item['image_path'], str)

    def test_empty_database_response(self):

        AlumniFace.objects.all().delete()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)