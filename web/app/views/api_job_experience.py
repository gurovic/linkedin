from rest_framework.views import APIView
from ..models import JobExperience
from ..serializers.job_experience_serializer import JobExperienceSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class JobExperienceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, _request):
        job_experiences = JobExperience.objects.all().order_by('-start_year')
        serializer = JobExperienceSerializer(job_experiences, many=True)
        return Response(serializer.data)
