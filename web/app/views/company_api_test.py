from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app.models.company import Company
from app.serializers.company_serializer import CompanySerializer


class CompanyViewTests(APITestCase):
    def setUp(self):
        self.company1 = Company.objects.create(
            name="Company 1",
            description="Description 1",
        )
        self.company2 = Company.objects.create(
            name="Company 2",
            description="Description 2",
        )
        self.valid_payload = {
            "name": "Company 3",
            "description": "Description 3",
        }
        self.invalid_payload = {
            "name": "",
            "description": "Description 4",
        }

    def test_get_all_companies(self):
        response = self.client.get(reverse("company"))
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_company(self):
        response = self.client.get(
            reverse("company", kwargs={"company_id": self.company1.id}),
        )
        company = Company.objects.get(id=self.company1.id)
        serializer = CompanySerializer(company)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

