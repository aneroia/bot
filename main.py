import telebot
from telebot import types
import datetime
import schedule
import time
from threading import Thread

bot = telebot.TeleBot("5690103487:AAEI8uDOaHv9DJR6wcSdYCCFXoZK9qeDg74")

for_help_file = open('for_help.txt', 'r', encoding='utf8')
for_help = for_help_file.read()
for_help_file.close()


def reminder(chat_id, timer):
    now_time = datetime.datetime.now()
    #end_time = now_time + time
    time.sleep(timer)
    bot.send_message(chat_id,text="Время вышло")



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🧾Составить список дел")
    btn2 = types.KeyboardButton("⏰Поставить таймер")
    btn3 = types.KeyboardButton("Посмотреть список дел")
    markup.add(btn1, btn2, btn3)
    bot.reply_to(message, for_help, reply_markup=markup)


def make_spisok(message):
    #bot.send_message(message.chat.id, message.text)
    dela.append(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить ещё")
    btn2 = types.KeyboardButton("Готово")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Это все дела на сегодня?", reply_markup=markup)

def get_dela_str(dela):
    spisok = ''
    for i in range(0, len(dela)):
        spisok += (str(i+1) + '. ' + dela[i] + '\n')
    return spisok


dela = ["popy pomoy"]

last_command = ""


@bot.message_handler(content_types=['text'])
def func(message):
    global last_command
    if message.text == "🧾Составить список дел" or message.text == "Добавить ещё":
        last_command = '🧾Составить список дел'
        bot.send_message(message.chat.id, text="Напиши, что тебе нужно сделать сегодня.")

        print(dela)

    elif message.text == "Готово":
        bot.send_message(message.chat.id, get_dela_str(dela))

    elif message.text == "⏰Поставить таймер":
        last_command = "⏰Поставить таймер"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("5 секунд")
        btn1 = types.KeyboardButton("10 минут")
        btn2 = types.KeyboardButton("30 минут")
        btn3 = types.KeyboardButton("Другое время")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0, btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="На сколько нужно завести таймер?", reply_markup=markup)


    elif message.text == "5 секунд":
        th = Thread(target=reminder(message.chat.id, 5))
        th.start()



    elif message.text == "Вернуться в главное меню":
        last_command = ""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🧾Составить список дел")
        btn2 = types.KeyboardButton("⏰Поставить таймер")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif last_command == "🧾Составить список дел":
        make_spisok(message)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# bot.reply_to(message, datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

bot.infinity_polling()
