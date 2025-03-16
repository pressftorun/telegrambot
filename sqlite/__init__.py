import telebot#тут у нас основное по sqlite,возможет говнокод
import sqlite3
from datetime import datetime
import pytz
from cfg import token
bot = telebot.TeleBot(token)
connection = sqlite3.connect('tasks.db',check_same_thread=False)#подключение к таблице
cursor = connection.cursor()#курсор
#создание таблицы если нет(при багах удалите старую просто)
cursor.execute('''
CREATE TABLE IF NOT EXISTS TASKS (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
time TEXT NOT NULL,
task TEXT NOT NULL
)
''')

def addnote(message):#добавление задач, пишет ник, время и само задние
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    cursor = connection.cursor()
    date = datetime.now()#Пишет время, в функции так как вне ее пишет не настоящее на момент записи, а время запуска бота
    cursor.execute('INSERT INTO TASKS (time,task,username) VALUES (?,?,?)', (date,message.text,message.from_user.username,))
    #добавление данных
    connection.commit()#сохранияем
    bot.send_message(message.chat.id, 'Добавлено задание:'+' '+message.text)#тот самый костыль
    
def giveinf(message):
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TASKS")#выбирает все
    a=cursor.fetchall()#выбирает все
    connection.commit()
    b=len(a)
    for i in range(0,b):#цикл для отправки каждого задания отдельно
        bot.send_message(message.chat.id,str(a[i]))#тот самый костыль

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()