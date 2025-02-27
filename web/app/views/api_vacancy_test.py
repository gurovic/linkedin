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
        self.company1 = Company.objects.create(name="Company 1", description="Company description 1",)
        self.company2 = Company.objects.create(name="Company 1", description="Company description 2",)
        self.major1 = Major.objects.create(name="Major 1")
        self.major2 = Major.objects.create(name="Major 2")
        self.language = Language.objects.create(name="English")
        self.vacancy1 = Vacancy.objects.create(
            name="Vacancy 1",
            description="Description 1",
            required_majors=self.major1.id,
            company=self.company1.id,
            expiration_date=timezone.now(),
            required_language=self.language.id,
            contacts='<EMAIL1>'
        )
        self.vacancy2 = Vacancy.objects.create(
            name="Vacancy 2",
            description="Description 2",
            required_majors=self.major2.id,
            company=self.company2.id,
            expiration_date=timezone.now(),
            required_language=self.language.id,
            contacts='<EMAIL2>'
        )

    def get_vacancy(self):
        serializer = VacancySerializer(vacancy_id=self.vacancy1.id)
        self.assertEqual(serializer.data, self.vacancy1.to_dict())

    def get_all_vacancies(self):
        url = reverse('all_vacancies')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]['name'], self.vacancy1.name)
        self.assertEqual(response.data[1]['name'], self.vacancy2.name)
