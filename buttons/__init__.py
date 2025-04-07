import telebot#кнопки тут чтоб не захламлять основной файл
from telebot import types
button1 = types.KeyboardButton('/dotask')
button2 = types.KeyboardButton('/lk')
button3 = types.KeyboardButton('/addadmin')
button4=types.KeyboardButton('blank')
button5 = types.KeyboardButton('/checktasks')
button6=types.KeyboardButton('blank')
admin1=types.KeyboardButton('/dotask')
admin2= types.KeyboardButton('/lk')
admin3 = types.KeyboardButton('/addtask')
admin4 = types.KeyboardButton('/checktasks')
admin5 = types.KeyboardButton('/deltask')
admin6 = types.KeyboardButton('/removeusers')