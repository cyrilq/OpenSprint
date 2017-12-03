import telebot
from telebot import types
import re
import requests
import time
import json
import logging
import html
from config import API_TOKEN
from consts import START_MESSAGE


bot = telebot.TeleBot(API_TOKEN)

logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start', 'help'])
def send(message):
    bot.send_message(message.chat.id, text=START_MESSAGE)


@bot.message_handler(commands=['inn'])
def send(message):
    if message.text[5:] == "":
        bot.send_message(message.chat.id, text="Проверьте правильность ввода")
    else:
        if True:
            nko_info = ("\n"
                        ""
                        "Есть ли у НКО Издание/вещательный канал: {}\n"
                        "Ссылка на карточку организации на портале Открытые НКО: {}\n"
                        "Лицензии на СМИ: {}\n"
                        "ИНН и ОГРН этой НКО: {}\n"
                        "Тип организации: {}\n"
                        "Статус организации (действующая/исключена): {}\n"
                        "Регион: {}\n"
                        "Территория распространения СМИ: {}\n"
                        "Язык(и) СМИ: {}\n"
                        "Форма выпуска: {}\n"
                        "Адрес сайта: {}\n"
                        "Ссылка на карточку СМИ на портале Открытые СМИ: {}\n"
                        "Перечень соучредителей, если таковые есть: {}\n"
                        "                ")
        pass


# polling cycle
if __name__ == '__main__':
    while True:
        logging.info('The polling cycle has started!')
        try:
            bot.polling(none_stop=True)
        except requests.exceptions.ConnectionError as e:
            logging.warning('There was requests.exceptions.ConnectionError')
            time.sleep(15)
