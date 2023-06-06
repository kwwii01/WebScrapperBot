import os

import telebot

from random_image import get_random_image

from dotenv import load_dotenv


load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Send any text message to receive random image.')

@bot.message_handler(content_types=['text'])
def send_random_image(message):
    image_to_send = get_random_image(message.text)
    with open(image_to_send, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

    os.remove(os.path.abspath(image_to_send))


@bot.message_handler(content_types=['sticker', 'photo', 'audio', 'video'])
def reply_to_invalid_content_type(message):
    bot.reply_to(message, 'Your message is not a text. Try again with something like "Sun"')
    with open('response.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    
bot.infinity_polling()