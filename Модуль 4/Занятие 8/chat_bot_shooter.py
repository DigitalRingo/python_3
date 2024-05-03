import random

import pyjokes
import telebot
import randfacts
from telebot import types
from deep_translator import GoogleTranslator
import requests
import shutil

# В это место нужно вставить токен своего бота!
API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)
# переводчик
translator = GoogleTranslator(source="auto", target="ru")

#случайный факт о числе
numbers_url = "http://numbersapi.com/"
#случайные картинки по категории природа (nature)
pictures_url = "https://api.api-ninjas.com/v1/randomimage?category=nature"
#ключ для API с картинками
pictures_api_key = "vX/WAHjtRF2exfGFIqpxUA==nhKATTvaGXf25oIm"

# список активных игроков
users = set()
# Статистика игры
# user_stat = {
#     "username": {"shots": 0, "stricken": 0},
#     "username2": {"shots": 0, "stricken": 0},
# }
user_stat = {}

actions = {
    "тапок": "Тапки полетели в @",
    "снежок": "Кидаю снежок в @",
    "лапка удачи": "Удар меховой лапкой с двойной силой по @",
    "лёд": "Удары фруктовыми кубиками льда по @"
}


# Активация взимодействия с ботом
# Сохранения активного пользователя
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # меню с началом шутера и кнопкой старт
    menu = types.ReplyKeyboardMarkup(row_width=2)

    start_button = types.KeyboardButton("/start")
    shooter_button = types.KeyboardButton("🥷 shooter 🥷")
    joke_button = types.KeyboardButton("😂 Анекдот 😂")
    fact_button = types.KeyboardButton("🤔 Факт 🤔")
    number_fact_button = types.KeyboardButton("🔢 Факт о числе 🔢")
    picture_button = types.KeyboardButton("🌅 Картинка 🌅")
    shots_button = types.KeyboardButton("/stat")
    help_button = types.KeyboardButton("/help")

    menu.add(start_button)
    menu.add(shooter_button)
    menu.add(joke_button)
    menu.add(fact_button)
    menu.add(number_fact_button)
    menu.add(picture_button)
    menu.add(shots_button)
    menu.add(help_button)

    # добавить сохранение пользователя в пользовательской базе бота
    current_user = message.from_user.username
    users.add(current_user)
    user_stat[current_user] = {"shots": 0, "stricken": 0}

    bot.reply_to(message,
                 f"Добро пожаловать в бота, {current_user}! Активные пользователи: {users}",
                 reply_markup=menu)


# обработк нажатия на кнопку с началом шутера, метод создания инлнайн-меню с шутером
@bot.message_handler(func=lambda message: message.text == "🥷 shooter 🥷")
def start_shooter(message):
    buttons = {
        "Кинуть тапком🩴": {"callback_data": "тапок"},
        "Кинуть снежком☃️": {"callback_data": "снежок"},
        "Двойной удар лапкой удачи🐾": {"callback_data": "лапка удачи"},
        "Замороженный лед❄️": {"callback_data": "лёд"}
    }
    menu = telebot.util.quick_markup(buttons, row_width=1)
    bot.reply_to(message, text="Shooter started", reply_markup=menu)


# обработка нажатия на кнопку в шутере
# отфильтровали пустые сообщения с lambda call: call.data
@bot.callback_query_handler(func=lambda call: call.data)
def make_shot(call):
    if len(users) > 0:
        victim_username = random.choice(list(users))
    else:
        victim_username = "unknown_user"

    # изменяем статистику
    # user_stat = {
    #     "username": {"shots": 0, "stricken": 0},
    #     "username2": {"shots": 0, "stricken": 0},
    # }
    action_username = call.from_user.username
    if action_username not in user_stat:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=f"Пользователь {action_username} не в игре",
        )

    user_stat[call.from_user.username]["shots"] += 1
    user_stat[victim_username]["stricken"] += 1
    # user_stat = {
    #     "username": {"shots": 1, "stricken": 0},
    #     "username2": {"shots": 0, "stricken": 1},
    # }

    message = actions.get(call.data) + victim_username
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.id,
        text=message,
    )


# команда вывода статистики в чат
@bot.message_handler(commands=["stat"])
def stat_handler(message):
    if not user_stat:
        bot.reply_to(message, "Игра еще не началась")
    else:
        # Статистика:
        # username1: выстрелов - 1, в игрока выстрелили - 2
        # username2: выстрелов - 2, в игрока выстрелили - 1
        output = "Статистика:"
        for username, stat in user_stat.items():
            stat_message = (
                f"{username}:  выстрелов - {stat['shots']}, "
                f"в игрока выстрелили - {stat['stricken']}"
            )
            output = f"{output}\n{stat_message}"

        bot.reply_to(message, output)


# случайная шутка
@bot.message_handler(func=lambda message: message.text == "😂 Анекдот 😂")
def joke_handler(message):
    joke = pyjokes.get_joke(category="chuck")
    ru_joke = translator.translate(joke)
    bot.reply_to(message, text=ru_joke)


# случайный факт
@bot.message_handler(func=lambda message: message.text == "🤔 Факт 🤔")
def fact_handler(message):
    fact = randfacts.get_fact()
    ru_fact = translator.translate(fact)
    bot.reply_to(message, text=ru_fact)


# возвращает случайный факт о числе в диапазоне от 0 до 10000
@bot.message_handler(func=lambda message: message.text == "🔢 Факт о числе 🔢")
def fact_number_handler(message):
    number = random.randint(0, 100)
    url = f"{numbers_url}{number}"
    response = requests.get(url=url)
    text_ru = translator.translate(response.text)
    bot.reply_to(message, text=text_ru)


# возвращает случайную картинку
@bot.message_handler(func=lambda message: message.text == "🌅 Картинка 🌅")
def picture_handler(message):
    response = requests.get(pictures_url,
                            headers={"X-Api-Key": pictures_api_key, "Accept": "image/jpg"},
                            stream=True)
    if response.status_code == requests.codes.ok:
        with open("img.jpg", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
            bot.send_photo(chat_id=message.chat.id, photo=open(out_file.name, "rb"))
    else:
        print("Error:", response.status_code, response.text)
        bot.reply_to(message, text="Ошибка при отправке изображения")


# Статистика агрессии: /shots
# username10 - 20 выстрела
# username1 - 2 выстрела
# username2 - 1 выстрела
# Статистика выживших: /alive
# username2 - 1 выстрела
# username1 - 2 выстрела
# username10 - 20 выстрела
@bot.message_handler(commands=["help"])
def help_handler(message):
    output = ("/start - зарегистрироваться в боте\n"
              "🥷 shooter 🥷 - шутер\n"
              "😂 Анекдот 😂 - случайный анекдот\n"
              "🤔 Факт 🤔 - случайный факт\n"
              "🔢 Факт о числе 🔢 - случайный факт о случайном числе от 0 до 100\n"
              "🌅 Картинка 🌅 - случайное изображение на тему\n"
              "/stat - показать статистику игры\n"
              "/help - информация о боте\n")
    bot.reply_to(message, output)


print("Бот запущен!")
bot.infinity_polling()
