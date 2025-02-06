from django.db.utils import IntegrityError
from django.test import TestCase

from app.models.major import Major


class MajorTest(TestCase):
    def setUp(self):
        self.major = Major(name="example")

    def test_major_creation(self):
        self.assertEqual(self.major.name, "example")

    def test_major_str(self):
        self.assertEqual(str(self.major), "example")

    def test_major_uniqueness(self):
        self.major.save()
        with self.assertRaises(IntegrityError):
            major = Major(name="example")
            major.save()
