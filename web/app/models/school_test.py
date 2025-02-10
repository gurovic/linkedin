from django.test import TestCase
from app.models import MajorSubject, School

class MajorSubjectModelTest(TestCase):

    def test_create_major_subject(self):
        major = MajorSubject.objects.create(subject='CS')
        self.assertEqual(major.subject, 'CS')
        self.assertEqual(str(major), 'Computer Science')

    def test_major_choices(self):
        for code, name in MajorSubject.MAJOR_CHOICES:
            major = MajorSubject(subject=code)
            self.assertEqual(major.get_subject_display(), name)


class SchoolModelTest(TestCase):

    def setUp(self):
        self.major_cs = MajorSubject.objects.create(subject='CS')
        self.major_math = MajorSubject.objects.create(subject='MATH')

    def test_create_school(self):
        school = School.objects.create(
            country='US',
            name='Harvard University',
            desc='A prestigious university.',
            lat=42.3770,
            lon=-71.1167
        )
        school.majors.set([self.major_cs, self.major_math])

        self.assertEqual(school.name, 'Harvard University')
        self.assertEqual(school.country, 'US')
        self.assertEqual(school.desc, 'A prestigious university.')
        self.assertEqual(str(school), 'Harvard University')
        self.assertEqual(school.lat, 42.3770)
        self.assertEqual(school.lon, -71.1167)
        self.assertQuerysetEqual(
            school.majors.all(),
            [self.major_cs, self.major_math],
            transform=lambda x: x
        )

    def test_optional_fields(self):
        school = School.objects.create(
            country='GB',
            name='Oxford University'
            # desc, lat, lon не заданы
        )
        self.assertIsNone(school.desc)
        self.assertIsNone(school.lat)
        self.assertIsNone(school.lon)
