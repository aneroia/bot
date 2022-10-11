import telebot
from telebot import types
import time
from threading import Thread

bot = telebot.TeleBot("токен бота")

for_help_file = open('for_help.txt', 'r', encoding='utf8')
for_help = for_help_file.read()
for_help_file.close()


def reminder(chat_id, timer):
    time.sleep(timer)
    if len(dela)!=0:
        bot.send_message(chat_id, text=("Время вышло 👺 \n" + get_dela_str(dela)))
    else:
        bot.send_message(chat_id, text="Время вышло 👺")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🧾Составить список дел")
    btn2 = types.KeyboardButton("⏰Поставить таймер")
    btn3 = types.KeyboardButton("👀Посмотреть список дел")
    markup.add(btn1, btn2, btn3)
    bot.reply_to(message, for_help, reply_markup=markup)

def set_time(message):
    timer = int(message.text)*60
    return timer
def make_spisok(message):
    dela.append(message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("✏Добавить ещё")
    btn2 = types.KeyboardButton("✅Готово")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Это все дела на сегодня?", reply_markup=markup)

def get_dela_str(dela):
    spisok = ('Список дел: \n')
    for i in range(0, len(dela)):
        spisok += (str(i+1) + '. ' + dela[i] + '\n')
    return spisok





dela = []

last_command = ""

def delete_delo(message):
    k = int(message.text)-1

    dela.pop(k)

@bot.message_handler(content_types=['text'])
def func(message):
    global last_command
    if message.text == "🧾Составить список дел" or message.text == "✏Добавить ещё":
        last_command = '🧾Составить список дел'
        bot.send_message(message.chat.id, text="Напиши, что тебе нужно сделать сегодня.")


    elif message.text == "✅Готово":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("🏠Вернуться в главное меню")
        markup.add(btn)
        bot.send_message(message.chat.id, get_dela_str(dela), reply_markup=markup)


    elif message.text == "⏰Поставить таймер":
        last_command = "⏰Поставить таймер"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn0 = types.KeyboardButton("5 секунд")
        btn1 = types.KeyboardButton("10 минут")
        btn2 = types.KeyboardButton("30 минут")
        btn3 = types.KeyboardButton("Другое время")
        back = types.KeyboardButton("🏠Вернуться в главное меню")
        markup.add(btn0, btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="На сколько нужно завести таймер?", reply_markup=markup)

######### ТАЙМЕРЫ
    elif message.text == "5 секунд":
        th = Thread(target=reminder(message.chat.id, 5))
        th.start()
    elif message.text == "10 минут":
        th = Thread(target=reminder(message.chat.id, 600))
        th.start()
    elif message.text == "30 минут":
        th = Thread(target=reminder(message.chat.id, 1800))
        th.start()
    elif message.text == "Другое время":
        last_command = 'Другое время'
        bot.send_message(message.chat.id, text="На сколько минут завести таймер?")
    elif last_command == "Другое время":
        last_command = "⏰Поставить таймер"
        th = Thread(target=reminder(message.chat.id, set_time(message)))
        th.start()



    elif message.text == "🏠Вернуться в главное меню":
        last_command = ""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🧾Составить список дел")
        btn2 = types.KeyboardButton("⏰Поставить таймер")
        btn3 = types.KeyboardButton("👀Посмотреть список дел")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif last_command == "🧾Составить список дел":
        make_spisok(message)

    elif message.text == "👀Посмотреть список дел" or last_command == "👀Посмотреть список дел":
        last_command = "👀Посмотреть список дел"
        if len(dela) == 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, text='У вас нет запланированных дел', reply_markup=markup)

        elif len(dela) > 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("❌Удалить дело из списка")
            btn2 = types.KeyboardButton("❌Очистить список дел")
            btn3 = types.KeyboardButton("🏠Вернуться в главное меню")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, get_dela_str(dela), reply_markup=markup)
            if message.text == "❌Удалить дело из списка":
                last_command = "❌Удалить дело из списка"
                bot.send_message(message.chat.id, text="Введите номер дела, которое хотите удалить")
            elif message.text == "❌Очистить список дел":
                last_command = "❌Очистить список дел"
                dela.clear()
                bot.send_message(message.chat.id, text="Список дел очищен!")

    elif last_command == "❌Удалить дело из списка":
        delete_delo(message)
        bot.send_message(message.chat.id, get_dela_str(dela))
        last_command = "👀Посмотреть список дел"








bot.infinity_polling()
