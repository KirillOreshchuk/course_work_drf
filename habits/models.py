from django.db import models

from config import settings
from config.settings import NULLABLE


class Habit(models.Model):
    """Модель привычки"""

    PERIODICITY_CHOICES = (
        ('1', 'ежедневно'),
        ('2', 'раз в два дня'),
        ('3', 'раз в три дня'),
        ('4', 'раз в четыре дня'),
        ('5', 'раз в пять дней'),
        ('6', 'раз в шесть дней'),
        ('7', 'раз в неделю'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    place = models.CharField(max_length=100, verbose_name='Место выполнения привычки')
    time = models.DateTimeField(verbose_name='Дата и время, когда необходимо выполнять привычку')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                      related_name='main_habit', verbose_name='Связанная привычка')
    periodicity = models.CharField(max_length=30, choices=PERIODICITY_CHOICES, default='1',
                                   verbose_name='Переодичность привычки')
    award = models.CharField(max_length=100, **NULLABLE, verbose_name='Вознаграждение за выполнение привычки')
    time_to_complete = models.SmallIntegerField(verbose_name='Время на выполнение привычки')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
