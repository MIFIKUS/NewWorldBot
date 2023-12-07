import telebot


TG_USER_ID = 123
TG_API_KEY = 123
BOT = telebot.TeleBot(TG_API_KEY)

def send_message(msg):
    """Функция для отпправки сообщения в тг"""
    self.BOT.send_message(TG_USER_ID, msg)
