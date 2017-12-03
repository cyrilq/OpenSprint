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
from get_info import GetInfo

bot = telebot.TeleBot(API_TOKEN)

logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start', 'help'])
def send(message):
    bot.send_message(message.chat.id, text=START_MESSAGE)


@bot.message_handler(commands=['info'])
def send(message):
    if message.text[6:] == "":
        bot.send_message(message.chat.id, text="Проверьте правильность ввода")
    else:
        inn = message.text[6:]
        gi = GetInfo(inn=inn).getInfo()
        if not gi['wrongINN']:
            nko_info, smi_info = "", ""
            if gi['haveMedia']:
                nko_info = ("\n"
                            "1. Название НКО: {}\n"
                            "2. Есть ли у НКО Издание/вещательный канал: {}\n"
                            "3. Ссылка на карточку организации на портале Открытые НКО: {}\n"
                            "4. ИНН: {}, ОГРН: {}\n"
                            "5. Тип организации: {}\n"
                            "6. Статус организации (действующая/исключена): {}\n"
                            "7. Регион: {}\n"
                            "5. Территория распространения СМИ: {}\n"
                            "6. Язык(и) СМИ: {}\n"
                            "7. Форма выпуска: {}\n"
                            "8. Адрес сайта: {}\n"
                            "9. Ссылка на карточку СМИ на портале Открытые СМИ: {}\n"
                            "10. Перечень соучредителей, если таковые есть: {}\n"
                            "=====================================\n"
                            "Доходы СМИ: {}"
                            "                ".format(gi['nameNKO'],
                                                      gi['haveMedia'],
                                                      gi['cartNKO'],
                                                      gi['INN'], gi['OGRN'],
                                                      gi['type'],
                                                      gi['active'],
                                                      gi['region'],
                                                      gi['territory'],
                                                      gi['languages'],
                                                      gi['formOutput'],
                                                      gi['web'],
                                                      gi['SMIcart'],
                                                      gi['nameNKO'],
                                                      gi['money_transfers_sum']))


                smi_info =("Контракт: {}\n"
                           "Грант: {}\n"
                           "Субсидия: {}\n"
                           "Ссылка на карточку: {}\n".format(gi['Contract'],
                                                   gi['Grant'],
                                                   gi['Subsidy'],
                                                   gi['cartNKO'],))
            else:
                nko_info = "НКО {} не является учредителем СМИ".format(gi['nameNKO'])
            bot.send_message(message.chat.id, nko_info, disable_notification=True)
            bot.send_message(message.chat.id, text=smi_info)

        else:
            bot.send_message(message.chat.id, text="Проверьте правильность ввода ИНН!")

        pass

@bot.message_handler(commands=['inn'])
def send(message):
    if message.text[5:] == "":
        bot.send_message(message.chat.id, text="Проверьте правильность ввода ИНН")
    else:
        inn = message.text[5:]
        pass

@bot.message_handler(commands=['reg'])
def send(message):
    if message.text[5:] == "":
        bot.send_message(message.chat.id, text="Проверьте правильность ввода региона")
    else:
        reg = message.text[5:]
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
