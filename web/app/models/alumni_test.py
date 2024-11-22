from unittest import TestCase
from unittest.mock import Mock
from app.models.alumni_model import Alumni

class TestAlumniModel(TestCase):
    def setUp(self):
        self.alumni = Mock(spec=Alumni)
        self.alumni.first_name = "John"
        self.alumni.last_name = "Doe"
        self.alumni.__str__.return_value = "John Doe"

    def test_str_method(self):
        self.assertEqual(str(self.alumni), "John Doe")