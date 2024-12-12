from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from web.app.serializers.user_serializer import UserSerializer, StudentSchoolSerializer, UniversityStudentSerializer
from ..models import StudentSchool, UniversityStudent

@api_view(['GET'])
def account_details(request, user_id):
    """
    API endpoint to fetch the account details of a user, including their 
    associated schools and universities. This endpoint will return data in
    JSON format, and only non-authenticated users can access this data.
    """

    try:
        # Fetch the user based on the provided user_id
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        # If the user does not exist, return a 404 error response
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the requested user matches the currently logged-in user (optional, for authorization)
    if user.id != request.user.id:
        # If the logged-in user is not the same as the requested user, return their data

        # Get all schools and universities associated with this user
        student_schools = StudentSchool.objects.filter(student=user)
        student_universities = UniversityStudent.objects.filter(student=user)

        # Serialize the user, school, and university data using the appropriate serializers
        user_data = UserSerializer(user)
        student_schools_data = StudentSchoolSerializer(student_schools, many=True)
        student_universities_data = UniversityStudentSerializer(student_universities, many=True)

        # Return a JSON response with the serialized data
        return Response({
            'user': user_data.data,
            'student_schools': student_schools_data.data,
            'student_universities': student_universities_data.data,
        })
    
    # If the user tries to access their own data, return a 403 Forbidden response
    return Response({'error': 'Unauthorized access'}, status=status.HTTP_403_FORBIDDEN)