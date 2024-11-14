from django.contrib.auth.models import User
from django.test import TestCase

from .school import School, MajorSubject
from .student_schools import StudentSchool


class StudentSchoolTestCase(TestCase):
    def setUp(self):
        student = User.objects.create(email="normal@user.com", password="foo")
        major = MajorSubject.objects.create(subject='А')
        school = School.objects.create(name="ГБОУ школа № 1", country='А', desc='А')
        school.majors.add(major)
        StudentSchool.objects.create(student=student, school=school, start_year=1,
                                     finish_year=1,
                                     why_left="GR")

    def test_StudentSchool_fields_correct(self):
        student = User.objects.get(email="normal@user.com", password="foo")
        StudentSchool1 = StudentSchool.objects.get(student=student)
        major = MajorSubject.objects.get(subject='А')
        school = School.objects.get(name="ГБОУ школа № 1", country='А', desc='А')
        school.majors.add(major)
        self.assertEqual(StudentSchool1.student, student)
        self.assertEqual(StudentSchool1.school, school)
        self.assertEqual(StudentSchool1.start_year, 1)
        self.assertEqual(StudentSchool1.finish_year, 1)
        self.assertEqual(StudentSchool1.why_left, "GR")
        self.assertEqual(str(StudentSchool1), f'{str(student)} at school {str(school)}')
