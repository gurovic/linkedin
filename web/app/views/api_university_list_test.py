from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from django.http.response import Http404

from ..serializers.small_university_serializer import SmallUniversitySerializer
from ..views.api_university_list import UniversityListView
from ..models import University


class UniversityListTests(APITestCase):
    def setUp(self):
        self.api = UniversityListView()

        self.uni1 = University.objects.create(
            name="Breakdance University",
            country="United Slates of America",
            lat=40,
            lon=-50
        )
        self.uni2 = University.objects.create(
            name="Unity College London",
            country="United Kingdom",
            lat=30,
            lon=0
        )

    def test_responses(self):
        response = self.api.get(None)
        json_data = response.data
        self.assertIn(SmallUniversitySerializer(self.uni1).data, json_data)
        self.assertIn(SmallUniversitySerializer(self.uni2).data, json_data)
