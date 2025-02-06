from django.db.utils import IntegrityError
from django.test import TestCase

from app.models.language import Language


class LanguageTest(TestCase):
    def setUp(self):
        self.language = Language(name="example")

    def test_language_creation(self):
        self.assertEqual(self.language.name, "example")

    def test_language_str(self):
        self.assertEqual(str(self.language), "example")

    def test_language_uniqueness(self):
        self.language.save()
        with self.assertRaises(IntegrityError):
            language = Language(name="example")
            language.save()
