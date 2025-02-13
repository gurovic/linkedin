from rest_framework import serializers

from app.models.universitystudent import UniversityStudent


class UniversityStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityStudent
        fields = (
            "id",
            "student",
            "university",
            "leave_reason",
            "start_year",
            "end_year",
        )
