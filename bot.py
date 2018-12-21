# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    markup = types.InlineKeyboardMarkup()
    itembtna = types.InlineKeyboardButton('Замовити лікаря чи кносультацію', switch_inline_query="")
    itembtnv = types.InlineKeyboardButton('Дізнатися статус заявки', switch_inline_query="")
    itembtnc = types.InlineKeyboardButton('Замовити :Перезвони мені:', switch_inline_query="")
    markup.row(itembtna)
    markup.row(itembtnv, itembtnc)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)