from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.company import Company
from app.serializers.company_serializer import CompanySerializer


class CompanyView(APIView):
    def get(self, request, company_id=None):
        if not company_id:
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
        else:
            companies = Company.objects.get(id=company_id)
            serializer = CompanySerializer(companies)
        return Response(serializer.data)
