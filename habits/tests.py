from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование эндпоинтов класса привычки"""

    def setUp(self) -> None:
        """ Подготовка к тестированию """
        self.user = User.objects.create(
            email='test@test.com',
            password='password_test',
            telegram_username='telegram_test',
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            place='На улице',
            time='2024-08-11T02:03:46Z',
            action='Пройти 1 км',
            is_pleasant=False,
            periodicity='7',
            award='Полежать 3 часа',
            time_to_complete=110,
            is_public=True,
            user=self.user
        )

    def test_list(self):
        """Тестирование вывода привычек пользователя"""

        response = self.client.get(reverse('habits:habit_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.habit.id,
                            'place': self.habit.place,
                            'time': self.habit.time,
                            'action': self.habit.action,
                            'is_pleasant': self.habit.is_pleasant,
                            'periodicity': self.habit.periodicity,
                            'award': self.habit.award,
                            'time_to_complete': self.habit.time_to_complete,
                            'is_public': self.habit.is_public,
                            'user': self.user.pk,
                            'related_habit': self.habit.related_habit
                        }
                    ]
            }

        )

    def test_list_public_habits(self):
        """Тестирование вывода публичных привычек"""

        response = self.client.get(reverse('habits:public_habit_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'id': self.habit.id,
                    'place': self.habit.place,
                    'time': self.habit.time,
                    'action': self.habit.action,
                    'is_pleasant': self.habit.is_pleasant,
                    'periodicity': self.habit.periodicity,
                    'award': self.habit.award,
                    'time_to_complete': self.habit.time_to_complete,
                    'is_public': self.habit.is_public,
                    'user': self.user.pk,
                    'related_habit': self.habit.related_habit
                }
            ]
        )

    def test_detail(self):
        """Тестирование отображения одной привычки"""

        response = self.client.get(reverse('habits:habit_detail', kwargs={'pk': self.habit.pk}))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'place': self.habit.place,
                'time': self.habit.time,
                'action': self.habit.action,
                'is_pleasant': self.habit.is_pleasant,
                'periodicity': self.habit.periodicity,
                'award': self.habit.award,
                'time_to_complete': self.habit.time_to_complete,
                'is_public': self.habit.is_public,
                'user': self.user.pk,
                'related_habit': self.habit.related_habit
            }
        )

    def test_create(self):
        """Тестирование создания привычки"""
        data = {
            'place': 'На работе',
            'time': '2024-08-11T02:03:46Z',
            'action': 'Присесть 100 раз',
            'is_pleasant': False,
            'periodicity': '7',
            'award': 'Полежать 7 часов',
            'time_to_complete': 50,
            'is_public': False
        }

        response = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'place': 'На работе',
                'time': '2024-08-11T02:03:46Z',
                'action': 'Присесть 100 раз',
                'is_pleasant': False,
                'periodicity': '7',
                'award': 'Полежать 7 часов',
                'time_to_complete': 50,
                'is_public': False,
                'user': self.user.pk,
                'related_habit': None,
            }
        )

    def test_update(self):
        """Тестирование изменения привычки"""

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.pk}),
            data={'time_to_complete': 50}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'place': self.habit.place,
                'time': self.habit.time,
                'action': self.habit.action,
                'is_pleasant': self.habit.is_pleasant,
                'periodicity': self.habit.periodicity,
                'award': self.habit.award,
                'time_to_complete': 50,
                'is_public': self.habit.is_public,
                'user': self.user.pk,
                'related_habit': self.habit.related_habit
            }
        )

    def test_delete(self):
        """Тестирование удаления привычки"""

        response = self.client.delete(reverse('habits:habit_delete', kwargs={'pk': self.habit.pk}))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
