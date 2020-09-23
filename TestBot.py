from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import sqlite3
import datetime


def sms(bot,update):
    print('Кто-то отправил мне команду /start что мне делать?')
    bot.message.reply_text('Привет,{}! \n'
                            'Рад держать тебя в курсе=) \n'
                            'Нажми запомнить для ввода новых событий или введи дату, на которую уже что-то запланированно'.format(bot.message.chat.first_name))

def remember(bot,update):
    print(bot.message.text)
    bot.message.reply_text('Введите дату в формате дд/мм и событие')


def answers(bot,update):
    if bot.message.text ==('18/09'):
        print(bot.message.text)
        bot.message.reply_text('День рождения!')

    elif bot.message.text ==('18/09 День рождения!'):
        print(bot.message.text)
        bot.message.reply_text('Готово')

    elif bot.message.text ==('20/06'):
        print(bot.message.text)
        bot.message.reply_text('Поездка на море')

    elif bot.message.text ==('20/06 Поездка на море'):
        print(bot.message.text)
        bot.message.reply_text('Готово')

    elif bot.message.text ==('01/09'):
        print(bot.message.text)
        bot.message.reply_text('День знаний')

    elif bot.message.text ==('01/09 День знаний'):
        print(bot.message.text)
        bot.message.reply_text('Готово')

    elif print(bot.message.text):
        bot.message.reply_text('Меньше слов, больше событий!')


def main():
    my_bot=Updater("1068204366:AAFmwPNfACRZmnkTfyUqXgmbZogi3z7kB7Q",use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start',sms))
    my_bot.dispatcher.add_handler(CommandHandler('z', remember))  # запомнить
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text,answers))
    my_bot.start_polling()
    my_bot.idle()

main()