from django.test import TestCase, Client
from django.urls import reverse

from .view_request import request_view
# from ..forms import StudentSchoolForm


class TestCreateStudentSchoolForm(TestCase):
    def test_get_request(self):
        client = Client()
        response = client.get(reverse('student_school_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/student_school_form.html')
        # self.assertIsInstance(response.context['form'], StudentSchoolForm)

    # def test_post_request_valid_form(self):
    #     client = Client()
    #     data = {'student': 'Иван Иванов', 'school': 'Школа №1', 'start_year': '01.01.2000', 'finish_year': '01.01.2000',
    #             'why_left': 'Graduated'}
    #     response = client.post(reverse('student_school_form'), data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, request_view)
    #
    # def test_post_request_invalid_form(self):
    #     client = Client()
    #     data = {'student': ''}
    #     response = client.post(reverse('student_school_form'), data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'app/student_school_form.html')
    #     self.assertIsInstance(response.context['form'], StudentSchoolForm)
