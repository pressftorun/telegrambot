import telebot#кнопки тут чтоб не захламлять основной файл
from telebot import types
button1 = types.KeyboardButton('Вчера')
button2 = types.KeyboardButton('Сегодня')
button3 = types.KeyboardButton('Завтра')
button4 = types.KeyboardButton('/start')
button5 = types.KeyboardButton('/addtask')
button6 = types.KeyboardButton('/help')
button7 = types.KeyboardButton('blank')
button8 = types.KeyboardButton('/checktasks')
button9 = types.KeyboardButton('/deltask')
