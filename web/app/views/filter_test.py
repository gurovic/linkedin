from django.test import TestCase
from django.contrib.auth.models import User
from app.models import UserSkill, Skill
from app.forms import SkillFilterForm
from django.urls import reverse


class SearchBySkillsTests(TestCase):
    def setUp(self):
        # Создаем тестовые навыки
        self.skill_python = Skill.objects.create(name="Python")
        self.skill_django = Skill.objects.create(name="Django")

        # Создаем пользователей
        self.user1 = User.objects.create(username="user1")
        self.user2 = User.objects.create(username="user2")

        # Связываем пользователей с навыками
        UserSkill.objects.create(user=self.user1, tag=self.skill_python)
        UserSkill.objects.create(user=self.user2, tag=self.skill_django)

    def test_view_renders_correct_template(self):
        """Проверка, что представление использует правильный шаблон."""
        response = self.client.get(reverse('search_by_skills'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/search_by_skills.html')

    def test_form_shows_skills(self):
        """Проверка, что форма показывает список навыков."""
        response = self.client.get(reverse('search_by_skills'))
        form = response.context['form']
        skills_in_form = list(form.fields['skills'].queryset)
        self.assertIn(self.skill_python, skills_in_form)
        self.assertIn(self.skill_django, skills_in_form)

    def test_search_by_single_skill(self):
        """Проверка фильтрации пользователей по одному навыку."""
        response = self.client.get(reverse('search_by_skills'), {'skills': [self.skill_python.id]})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user1, response.context['userskills'])
        self.assertNotIn(self.user2, response.context['userskills'])

    def test_search_by_multiple_skills(self):
        """Проверка фильтрации пользователей по нескольким навыкам."""
        response = self.client.get(reverse('search_by_skills'), {'skills': [self.skill_python.id, self.skill_django.id]})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user1, response.context['userskills'])
        self.assertIn(self.user2, response.context['userskills'])

    def test_no_skills_selected(self):
        """Проверка поведения, если навыки не выбраны."""
        response = self.client.get(reverse('search_by_skills'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['userskills'])

    def test_empty_result(self):
        """Проверка поведения, если нет пользователей с выбранными навыками."""
        new_skill = Skill.objects.create(name="NonexistentSkill")
        response = self.client.get(reverse('search_by_skills'), {'skills': [new_skill.id]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['userskills']), 0)