from rest_framework import serializers

from habits.models import Habit


class OnlyRelatedOrAwardValidator:
    """Валидатор, который исключает одновременный выбор связанной привычки и вознаграждения"""

    def __call__(self, value):
        related_habit = dict(value).get('related_habit')
        award = dict(value).get('award')
        if related_habit and award:
            raise serializers.ValidationError(
                'Ошибка! Одновременно выбрана связанная привычка и вознааграждение.'
            )


class TimeToCompleteValidator:
    """Валидатор, который проверяет что время выполнения должно быть не больше 120 секунд"""

    def __call__(self, value):
        if int(dict(value).get('time_to_complete')) > 120:
            raise serializers.ValidationError(
                'Ошибка! Время выполнения привычки более 120 секунд.'
            )


class RelatedHabitIsPleasantValidator:
    """Валидотор, который проверяет, что связанные привычки могут попадать
    только привычки с признаком приятной привычки."""

    def __call__(self, value):
        related_habit = dict(value).get('related_habit')

        if related_habit:
            habit = Habit.objects.get(pk=related_habit.id)
            if not habit.is_pleasant:
                raise serializers.ValidationError(
                    'Ошибка! Связанная привычка должна иметь признак приятной привычки.'
                )


class PleasantValidator:
    """Валидатор, который проверяет, что у приятной привычки не может быть вознаграждения или связанной привычки. """

    def __call__(self, value):
        related_habit = dict(value).get('related_habit')
        award = dict(value).get('award')
        is_pleasant = dict(value).get('is_pleasant')

        if is_pleasant and award or is_pleasant and related_habit:
            raise serializers.ValidationError(
                'Ошибка! У приятной привычки не может быть вознаграждения или связанной привычки.'
            )

# Валидатор, который проверяет, что нельзя выполнять привычку реже,
# чем 1 раз в 7 дней - реализован на уровне полей модели с помощью 'PERIODICITY_CHOICES'
