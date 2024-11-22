from unittest import TestCase
from unittest.mock import Mock, patch
from app.views.view_api import AlumniListView
from app.serializers.AlumniSerializer import AlumniSerializer

class TestAlumniListView(TestCase):
    @patch('app.models.alumni_model.Alumni.objects')
    def test_get_queryset(self, mock_objects):
        mock_alumni = Mock()
        mock_alumni.first_name = "John"
        mock_objects.all.return_value = [mock_alumni]

        view = AlumniListView()
        queryset = view.get_queryset()

        self.assertEqual(len(queryset), 1)
        self.assertEqual(queryset[0].first_name, "John")