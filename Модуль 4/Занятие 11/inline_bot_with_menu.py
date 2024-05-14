from hugchat import hugchat
from hugchat.login import Login
from telebot import types

import telebot
import datetime

# токен бота
API_TOKEN = ""
bot = telebot.TeleBot(API_TOKEN)

# почта на https://huggingface.co/
HUGGING_FACE_EMAIL = ""
# пароль от аккаунта на https://huggingface.co/
HUGGING_FACE_PASSWORD = ""

cookie_path_dir = "./cookies/"
sign = Login(HUGGING_FACE_EMAIL, HUGGING_FACE_PASSWORD)


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
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
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
bot.polling()
