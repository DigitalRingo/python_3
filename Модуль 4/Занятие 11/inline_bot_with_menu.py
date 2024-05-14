from os import getenv
from hugchat import hugchat
from hugchat.login import Login
from telebot import types

import telebot
import datetime

API_TOKEN = "7058112558:AAEkGixjtIp1QLTmoMUI-7tF9ZmymvVDVAs"
bot = telebot.TeleBot(getenv('API_TOKEN') or API_TOKEN)

HUGGING_FACE_EMAIL = "digitalringo@gmail.com"
HUGGING_FACE_PASSWORD = "cQCzQS:r#Ea45+."

cookie_path_dir = "./cookies/"
sign = Login(HUGGING_FACE_EMAIL, HUGGING_FACE_PASSWORD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

# Добавляем логирование входящих сообщений
@bot.message_handler(func=lambda message: True)
def log_message(message):
    print(
        f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
        f"новое сообщение от: {message.from_user.last_name} {message.from_user.first_name} "
        f"aka @{message.from_user.username} ,"
        f" текст: {message.text}"
    )
    return telebot.ContinueHandling()


@bot.message_handler(func=lambda message: True)
def handle_private_message(message):
    response = get_ai_response(message.text)
    bot.send_message(message.chat.id, response)


# Добавляем инлайн обработчик
@bot.inline_handler(func=lambda query: "?" in str(query.query))
def handle_inline_question(query):
    try:
        prompt = query.query
        message = get_ai_response(prompt)
        answer = types.InlineQueryResultArticle(
            id="1",
            title="AI helper",
            description=message,
            input_message_content=types.InputTextMessageContent(
                message_text=message
            )
        )
        bot.answer_inline_query(query.id, [answer])
    except Exception as exception:
        print(exception)

# метод для получения ответа от AI
def get_ai_response(query):
    prompt = query.strip()
    response = chatbot.chat(prompt)
    return str(response)


bot.set_my_commands(
    [
        types.BotCommand(
            command="start", description="Начать работу"
        ),
        types.BotCommand(
            command="about", description="Описание работы бота"
        )
    ]
)
print("Бот стартовал!")
bot.polling(timeout=100, long_polling_timeout=100)
