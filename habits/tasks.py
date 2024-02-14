from datetime import timedelta

from django.utils import timezone
from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_notification():
    """Переодическая задача для отправки уведомления"""

    habits = Habit.objects.all()
    time_now = timezone.now()

    for habit in habits:
        if time_now >= habit.time - timedelta(minutes=15):
            message = (f'Я буду {habit.action} в {habit.time} в {habit.place} за это я могу:'
                       f' {habit.related_habit if habit.related_habit else habit.award} ')

            send_telegram_message(
                chat_id=habit.user.telegram_chat_id,
                message=message
            )

            habit.time += timedelta(days=int(habit.periodicity))
            habit.save()
