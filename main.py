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


@bot.message_handler(commands=['info'])
def send(message):
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
