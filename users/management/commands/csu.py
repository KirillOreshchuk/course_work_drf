import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            first_name='Admin',
            last_name='Adminov',
            telegram_username='Admin_tg',
            telegram_chat_id=os.getenv('CHAT_ID_TG'),
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('12345678')
        user.save()
