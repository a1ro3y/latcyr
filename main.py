from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = '5377214882:AAGnVC7wKE4REXdGcocsidmPov4rqYRvg_4'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Xush kelibsiz!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    answer = lambda msg: to_cyrillic(msg) if msg.isaccii() else to_latin(msg)
    bot.reply_to(message, answer(msg))


bot.polling()
