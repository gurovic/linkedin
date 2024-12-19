from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .search import user_search

class UserSearchViewTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', first_name='Stephen', last_name='Curry')
        self.user2 = User.objects.create_user(username='testuser2', first_name='Kevin', last_name='Durant')
        self.user3 = User.objects.create_user(username='testuser3', first_name='LeBron', last_name='James')

    def test_last_name(self):
        response = self.client.get(reverse('user_search'), {'query': 'curry'})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Curry Stephen')
        self.assertNotContains(response, 'Durant Kevin')
        self.assertNotContains(response, 'James LeBron')

    def test_first_name(self):
        response = self.client.get(reverse('user_search'), {'query': 'Steph'})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Curry Stephen')
        self.assertNotContains(response, 'Durant Kevin')
        self.assertNotContains(response, 'James LeBron')

    def test_first_last_name(self):
        response = self.client.get(reverse('user_search'), {'query': 'Stephen curry'})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Curry Stephen')

    def test_last_first_name(self):
        response = self.client.get(reverse('user_search'), {'query': 'curry Stephen'})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Curry Stephen')

    def test_partial_query(self):
        response = self.client.get(reverse('user_search'), {'query': '   EN Cu '})
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Curry Stephen')
        self.assertNotContains(response, 'Durant Kevin')
        self.assertNotContains(response, 'James LeBron')

    def test_no_results(self):
        response = self.client.get(reverse('user_search'), {'query': 'Russ'})
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, 'Curry Stephen')
        self.assertContains(response, 'No users found.')

    def test_empty_query(self):
        response = self.client.get(reverse('user_search'), {'query': '   '})
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, 'Curry Stephen')
        self.assertContains(response, 'No users found.')

    def test_multiple_results(self):
        response = self.client.get(reverse('user_search'), {'query': 'a'})
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, 'Curry Stephen')
        self.assertContains(response, 'Durant Kevin')
        self.assertContains(response, 'James LeBron')
