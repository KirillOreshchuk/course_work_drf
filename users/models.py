from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта пользователя')

    telegram_username = models.CharField(max_length=100, unique=True, verbose_name='Имя пользователя Telegram')
    telegram_chat_id = models.IntegerField(unique=True, **NULLABLE, verbose_name='ID чата Telegram')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
