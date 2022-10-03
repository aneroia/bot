import telebot
from telebot import types
import datetime

bot = telebot.TeleBot("5690103487:AAEI8uDOaHv9DJR6wcSdYCCFXoZK9qeDg74")

for_help_file = open('for_help.txt','r',encoding='utf8')
for_help = for_help_file.read()
for_help_file.close()
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🧾Составить список дел")
    btn2 = types.KeyboardButton("⏰Поставить таймер")
    btn3 = types.KeyboardButton("Посмотреть список дел")
    markup.add(btn1, btn2, btn3)
    bot.reply_to(message, for_help, reply_markup=markup)



dela = ['popy pomoy']

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🧾Составить список дел"):
        bot.send_message(message.chat.id, text="Напиши, что тебе нужно сделать сегодня.")

        #@bot.message_handler(content_types=['text'])
        @bot.message_handler(func=lambda message: True)
        def make_spisok(message):
            bot.send_message(message.chat.id, message.text)
            dela.append(message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Добавить ещё")
            btn2 = types.KeyboardButton("Готово")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="Это все дела на сегодня?", reply_markup=markup)



        print(dela)



        #if (len(dela) == 1):
            #bot.send_message(message)
            #markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            #btn1 = types.KeyboardButton("Добавить ещё")
            #btn2 = types.KeyboardButton("Готово")
            #markup.add(btn1, btn2)

            #bot.reply_to(message, text="Это все дела на сегодня?", reply_markup=markup)

    elif(message.text == "⏰Поставить таймер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("10 минут")
        btn2 = types.KeyboardButton("30 минут")
        btn3 = types.KeyboardButton("Другое время")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="На сколько нужно завести таймер?", reply_markup=markup)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🧾Составить список дел")
        btn2 = types.KeyboardButton("⏰Поставить таймер")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
    #bot.reply_to(message, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

bot.infinity_polling()
