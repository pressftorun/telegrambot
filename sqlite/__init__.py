import telebot
import sqlite3
from datetime import datetime
import pytz
from cfg import token
bot = telebot.TeleBot(token)
connection = sqlite3.connect('tasks.db',check_same_thread=False)
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS TASKS (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
time TEXT NOT NULL,
task TEXT NOT NULL
)
''')

def addnote(message):
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    cursor = connection.cursor()
    date = datetime.now()
    cursor.execute('INSERT INTO TASKS (time,task,username) VALUES (?,?,?)', (date,message.text,message.from_user.username,))
    connection.commit()
    bot.send_message(message.chat.id, 'Добавлено задание:'+' '+message.text)


# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()