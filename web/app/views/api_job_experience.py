from rest_framework.views import APIView
from ..models import JobExperience
from ..serializers.job_experience_serializer import JobExperienceSerializer
from rest_framework.response import Response


class JobExperienceView(APIView):
    def get(self, _request):
        job_experiences = JobExperience.objects.all()
        serializer = JobExperienceSerializer(job_experiences, many=True)
        return Response(serializer.data)
