from django.contrib.auth.models import User
from django.test import TestCase

from app.models import University, UniversityStudent
from app.serializers import UserDetailSerializer


class UserDetailSerializerTests(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass', first_name='Test',
                                             last_name='User')

        # Create a university
        self.university = University.objects.create(name='Test University')

        # Create a UniversityStudent relationship
        UniversityStudent.objects.create(student=self.user, university=self.university, start_date="2024-10-10")

    def test_serializer_with_university(self):
        serializer = UserDetailSerializer(self.user)
        data = serializer.data

        self.assertEqual(data['first_name'], self.user.first_name)
        self.assertEqual(data['last_name'], self.user.last_name)
        self.assertEqual(len(data['university']), 1)
        self.assertEqual(data['university'][0]['name'], self.university.name)

    def test_serializer_without_university(self):
        # Create another user without a university
        another_user = User.objects.create_user(username='anotheruser', password='testpass', first_name='Another',
                                                last_name='User')
        serializer = UserDetailSerializer(another_user)
        data = serializer.data

        self.assertEqual(data['first_name'], another_user.first_name)
        self.assertEqual(data['last_name'], another_user.last_name)
        self.assertEqual(data['university'], [])