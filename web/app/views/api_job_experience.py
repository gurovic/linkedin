from rest_framework.views import APIView
from ..models import JobExperience
from ..serializers.job_experience_serializer import JobExperienceSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class JobExperienceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = request.query_params.get('user_id')

        if user_id:
            queryset = JobExperience.objects.filter(user_id=user_id)
        else:
            queryset = JobExperience.objects.filter(user=request.user)
        queryset = queryset.order_by('-start_year')
        serializer = JobExperienceSerializer(queryset, many=True)
        return Response(serializer.data)
