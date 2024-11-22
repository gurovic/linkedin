from unittest import TestCase
from unittest.mock import Mock
from app.serializers.AlumniSerializer import AlumniSerializer

class TestAlumniSerializer(TestCase):
    def test_valid_data(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'university': 'Test University'
        }
        serializer = AlumniSerializer(data=data)
        self.assertTrue(serializer.is_valid())