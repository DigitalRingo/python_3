import telebot
from telebot import types
import datetime
import random

# В это место нужно вставить токен своего бота!
API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)
users = set()
actions = {
    "тапок": "Тапки полетели в @",
    "снежок": "Кидаю снежок в @",
    "лапка удачи": "Удар меховой лапкой с двойной силой по @",
    "лёд": "Удары фруктовыми кубиками льда по @"
}


# Добавляем логирование входящих сообщений
@bot.message_handler(func=lambda message: True)
def log_message(message):
    print(
        f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} "
        f"новое сообщение от: {message.from_user.last_name} {message.from_user.first_name} "
        f"aka @{message.from_user.username} ,"
        f" текст: {message.text}"
    )
    return telebot.ContinueHandling()


# Активация взимодействия с ботом
# Сохранения активного пользователя
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # меню с началом шутера и кнопкой старт
    menu = types.ReplyKeyboardMarkup(row_width=2)
    start_button = types.KeyboardButton("/start")
    shooter_button = types.KeyboardButton("🥷 shooter 🥷")
    menu.add(start_button)
    menu.add(shooter_button)

    # добавить сохранение пользователя в пользовательской базе бота
    current_user = message.from_user.username
    users.add(current_user)

    bot.reply_to(message,
                 f"Добро пожаловать в бота, {current_user}! Активные пользователи: {users}",
                 reply_markup=menu)


# обработк нажатия на кнопку с началом шутера, метод создания инлнайн-меню с шутером
@bot.message_handler(func=lambda message: message.text == "🥷 shooter 🥷")
def start_shooter(message):
    buttons = {
        "Кинуть тапком🩴": {"callback_data": "тапок"},
        "Кинуть снежком": {"callback_data": "снежок"},
        "Двойной удар лапкой удачи": {"callback_data": "лапка удачи"},
        "Замороженный лед": {"callback_data": "лёд"},
        "Загуглить": {"url": "http://google.com"}
    }
    menu = telebot.util.quick_markup(buttons, row_width=1)
    bot.reply_to(message, text="Shooter started", reply_markup=menu)


# обработка нажатия на кнопку в шутере
@bot.callback_query_handler(func=lambda call: True)
def make_shot(call):
    message = ""
    if len(users) > 0:
        username = random.choice(list(users))
    else:
        username = "unknown_user"
    if call.data is not None:
        message = actions.get(call.data) + username
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=message)

# добавить статистику по активностям


print("Бот запущен!")
bot.infinity_polling()
