import telebot#тут у нас основное по sqlite,возможет говнокод
import sqlite3
from datetime import datetime
import pytz
from needdisp import daymnedan
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
    try:
        connection = sqlite3.connect('tasks.db',check_same_thread=False)
        cursor = connection.cursor()
        date = datetime.now()#Пишет время, в функции так как вне ее пишет не настоящее на момент записи, а время запуска бота
        cursor.execute('INSERT INTO TASKS (time,task,username) VALUES (?,?,?)', (date,message.text,message.from_user.username,))
        #добавление данных
        connection.commit()#сохранияем
        connection.close()
        bot.send_message(message.chat.id, 'Добавлено задание:'+' '+message.text)#тот самый костыль
    except ValueError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection.commit()
        connection.close()
    except TypeError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection.commit()
        connection.close()
    except sqlite3.IntegrityError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection.commit()
        connection.close()
def getnumbers():
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    cursor = connection.cursor()
    result = cursor.execute("SELECT id FROM TASKS").fetchall()
    cleanstr=''
    for i in range(0,len(result)):
        tupla=str(result[i])
        clean1=tupla.replace('(','')
        clean2=clean1.replace(',','')
        clean3=clean2.replace(')','')
        if i==len(result)-1:
            cleanstr=cleanstr+clean3
        else:  
            cleanstr=cleanstr+clean3+','
    return cleanstr
    
def giveinf(message):
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TASKS")#выбирает все
    a=cursor.fetchall()#выбирает все
    connection.commit()
    b=len(a)
    if b==0:
        bot.send_message(message.chat.id,'Нету записей в базе данных')
    else:
        cursor.execute("SELECT * FROM TASKS WHERE id = "+str(message.text))#выбирает все
        a=cursor.fetchall()#выбирает все
        connection.commit()
        daymnedan(message)#тот самый костыль
def deleteinf(message):
    try:
        connection = sqlite3.connect('tasks.db',check_same_thread=False)
        cursor = connection.cursor()
        delid= int(message.text)
        todelete='DELETE from TASKS where id = '+str(delid)
        cursor.execute(todelete)
        connection.commit()
        bot.send_message(message.chat.id,'Удалена запись №: '+ str(delid))
    except ValueError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection.commit()
        connection.close()
    except TypeError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection.commit()
        connection.close()
# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()