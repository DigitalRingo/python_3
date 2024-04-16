import telebot
from telebot import types
import datetime
import random

#В это место нужно вставить токен своего бота!
API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)

greetings = {"ПРИВЕТ", "ЗДРАВСТВУЙ", "ДОБРЫЙ ДЕНЬ"}
new_words = [
    "Селфи - это Слово происходит от английского возвратного суффикса -self, означающего отношение к себе и аналогичного русскому суффиксу «-сь» в словах: «моюсь», «возвращаюсь» и других. Они, в свою очередь, ни что иное, как сокращение от слова «себя», то есть «мою себя», «возвращаю себя» и так далее.",
    "Репост - Одна из функций абсолютно всех соцсетей — это возможность делать репосты сообщений, то есть размещать чужой пост (публикацию, сообщение) на своей странице, разумеется, со ссылкой на источник, которая прописывается автоматически, либо прислать ссылку на чужой пост адресно кому-то из своих подписчиков"
]


# Добавляем логирование входящих сообщений
@bot.message_handler(func=lambda message: True)
def log_message(message):
    print(
        f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} "
        f"новое сообщение от: {message.chat.last_name} {message.chat.first_name} aka @{message.chat.username},"
        f" текст: {message.text}"
    )
    return telebot.ContinueHandling()


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Добро пожаловать в бота, {message.chat.username}!")


# Обрабатывает приветствие пользователя
@bot.message_handler(func=lambda message: greetings.issuperset({message.text.upper()}))
def send_greetings(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}!")


# Отвечает на запрос про значение случайного слова
@bot.message_handler(commands=["new_word"])
def send_new_word(message):
    bot.reply_to(message, get_new_word())


def get_new_word():
    index = random.randint(0, len(new_words) - 1)
    random_word = new_words[index]
    return random_word


print("Бот запущен!")
bot.infinity_polling()
