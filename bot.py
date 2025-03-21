from cfg import token#импорт кода других папок и модулей
import telebot,sqlite3
from needdisp import daymnedan
from sqlite3 import Error
from sqlite import addnote,giveinf,deleteinf,getnumbers
from buttons import button1, button2, button3,button4,button5,button6,button7,button8,button9
from telebot import types
bot = telebot.TeleBot(token)#токен бота,ВАЖНО!
@bot.message_handler(commands = ['start'])#команда старт(по коду, то что после собаки-условие, вызывающее функцию под ним)
def handle_start(message):
  keyboard = types.ReplyKeyboardMarkup(row_width=3)#тип клавы, ширина
  keyboard.add(button1, button2, button3,button4,button5,button6,button7,button8,button9)
  bot.reply_to(message, 'Привет! Прокликай кнопки.', reply_markup=keyboard)#непосредственно добавляет клаву

@bot.message_handler(commands = ['help'])
def helpfunc(message):
    bot.send_message(message.chat.id, 'Привет, напиши слово СЕГОДНЯ, ЗАВТРА или ВЧЕРА')

@bot.message_handler(commands = ['checktasks'])
def helpfunc(message):
    bot.send_message(message.chat.id, 'Введите номер задания из списка: '+str(getnumbers()))
    bot.register_next_step_handler(message,giveinf)
    

@bot.message_handler(commands = ['addtask'])
def helpfunc(message):
    bot.send_message(message.chat.id, 'Введите задание')
    bot.register_next_step_handler(message,addnote)#тут у нас отсылка сообщения в файле sqlite, потом ответ отттуда же(костыль)
@bot.message_handler(commands = ['deltask'])
def delfunc(message):
    bot.send_message(message.chat.id, 'Введите номер задания для удаления')
    bot.register_next_step_handler(message,deleteinf)
#принимает сообщения на постоянке, если нет обращения к командам типа /...(СТАВИТЬ В САМЫЙ НИЗ)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower()=='сегодня':
        bot.send_message(message.chat.id, 'Сегодня день Сегодня')
    elif message.text.lower()=='завтра':
        bot.send_message(message.chat.id, 'Завтра будет Завтра')
    elif message.text.lower()=='вчера':
        bot.send_message(message.chat.id, 'Вчера было Вчера')
    else:
        bot.reply_to(message, 'Чет не то ты написал...')

bot.polling(none_stop = True)#цикл работы бота(чтоб не отключался(он отключится после 5 минут афк где-то))
