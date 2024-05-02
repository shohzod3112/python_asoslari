#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:34:02 2024
КИРИЛЛ-LOTIN TELEGRAM BOT
@author: moon
"""
import telebot

from transliterate import to_cyrillic, to_latin
TOKEN = '6764554642:AAH6Ghcp5G4HctMgaLcGtYMSf7dVyZyv6o8nw'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    javob = "Assalomu Aleykum, Xush kelibsiz!"
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    bot.reply_to(message, javob(msg))     

bot.infinity_polling()


# matn = input("Matn kiriting:")

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
