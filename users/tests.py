from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    """Тестирование модели пользователя"""

    def setUp(self) -> None:
        self.data = {
            'email': 'test@test.ru',
            'telegram_username': 'tg_test',
            'telegram_chat_id': 'tg_chat_id_test',
            'password': 'test',
            'password2': 'test'
        }

    def test_user_registration(self):
        """Тестирование регистрации пользователя"""

        response = self.client.post(reverse('users:user_registration'), data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
