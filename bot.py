from cfg import token
import telebot,sqlite3
from sqlite3 import Error
from sqlite import addnote
from buttons import button1, button2, button3,button4,button5,button6
from telebot import types
bot = telebot.TeleBot(token)


@bot.message_handler(commands = ['start'])
def handle_start(message):
  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(row_width=3)
  keyboard.add(button1, button2, button3,button4,button5,button6)
  # Отправка сообщения с клавиатурой
  bot.reply_to(message, 'Привет! Прокликай кнопки.', reply_markup=keyboard)

@bot.message_handler(commands = ['help'])
def helpfunc(message):
    bot.send_message(message.chat.id, 'Привет, напиши слово СЕГОДНЯ, ЗАВТРА или ВЧЕРА')

@bot.message_handler(commands = ['addtask'])
def helpfunc(message):
    bot.send_message(message.chat.id, 'Введите задание')
    bot.register_next_step_handler(message,addnote)
    
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


bot.polling(none_stop = True)
