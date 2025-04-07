from django.test import TestCase
from django.contrib.auth.models import User
from .user_search import UserSearch

class UserSearchTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            first_name='Иван',
            last_name='Петров',
            email='ivan@example.com'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            first_name='Мария',
            last_name='Сидорова',
            email='maria@example.com'
        )
        self.user3 = User.objects.create_user(
            username='user3',
            first_name='Алексей',
            last_name='Иванов',
            email='alex@example.com'
        )

    def test_search_by_first_name(self):
        results = UserSearch.user_search(self, query='Иван')
        self.assertQuerySetEqual(results, [self.user1, self.user3], transform=lambda x: x, ordered=False)

    def test_search_by_last_name(self):
        results = UserSearch.user_search(self, query='Сидорова')
        self.assertQuerySetEqual(results, [self.user2], transform=lambda x: x)

    def test_search_by_partial_name(self):
        results = UserSearch.user_search(self, query='Иван')
        self.assertIn(self.user1, results)
        self.assertNotIn(self.user2, results)

    def test_search_by_full_name(self):
        results = UserSearch.user_search(self, query='Иван Петров')
        self.assertQuerySetEqual(results, [self.user1, self.user3], transform=lambda x: x, ordered=False)

    def test_search_by_first_word_of_query(self):
        results = UserSearch.user_search(self, query='Иван Петрович')
        self.assertIn(self.user1, results)

    def test_search_by_last_word_of_query(self):
        results = UserSearch.user_search(self, query='Петрович Иван')
        self.assertIn(self.user1, results)


    def test_empty_search(self):
        results = UserSearch.user_search(self, query=None)
        self.assertEqual(results.count(), 3)
