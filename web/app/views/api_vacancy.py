from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from ..models.company import Vacancy
from ..serializers.vacancy_api import VacancySerializer
from rest_framework.views import APIView


class VacancyView(APIView):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
