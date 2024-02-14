from rest_framework import serializers

from habits.models import Habit
from habits.validators import (OnlyRelatedOrAwardValidator, TimeToCompleteValidator, RelatedHabitIsPleasantValidator,
                               PleasantValidator)


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор модели привычки"""
    validators = [
        OnlyRelatedOrAwardValidator(),
        TimeToCompleteValidator(),
        RelatedHabitIsPleasantValidator(),
        PleasantValidator(),
    ]

    class Meta:
        model = Habit
        fields = '__all__'
