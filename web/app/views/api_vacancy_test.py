from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APITestCase
from ..models.company import Vacancy
from ..serializers.vacancy_serializer import VacancySerializer
from ..models.company import Company
from ..models.major import Major
from ..models.language import Language



class VacancyApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.company = Company.objects.create(name="Company 1", description="Description 1",)
        self.major = Major.objects.create(name="Major 1")
        self.language = Language.objects.create(name="English")
        self.vacancy = Vacancy.objects.create(
            name="Vacancy 1",
            description="Description 1",
            required_majors=self.major.id,
            company=self.company.id,
            expiration_date=timezone.now(),
            required_language=self.language.id,
            contacts='<EMAIL>'
        )

    def get_vacancy(self):
        serializer = VacancySerializer(vacancy_id=self.vacancy.id)
        self.assertEqual(serializer.data, self.vacancy.to_dict())