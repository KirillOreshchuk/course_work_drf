import requests
from dotenv import load_dotenv
import os

load_dotenv()


def send_telegram_message(chat_id, message):
    """Отправка сообщения в Telegram"""
    tg_url = f'https://api.telegram.org/bot{os.getenv("TG_BOT_API")}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url=tg_url, params=params)
    return response.json()
