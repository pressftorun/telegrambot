import telebot#тут у нас основное по sqlite,возможет говнокод
import sqlite3
from buttons import *
from datetime import datetime
import pytz
from needdisp import daymnedan
from cfg import token
bot = telebot.TeleBot(token)
connection = sqlite3.connect('tasks.db',check_same_thread=False)#подключение к таблице
connection2 = sqlite3.connect('admins.db',check_same_thread=False)#подключение к таблице
cursor = connection.cursor()#курсор
cursor2 = connection2.cursor()#курсор
#создание таблицы если нет(при багах удалите старую просто)
cursor.execute('''
CREATE TABLE IF NOT EXISTS TASKS (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
time TEXT NOT NULL,
task TEXT NOT NULL,
anwser TEXT NOT NULL
)
''')
cursor2.execute('''
CREATE TABLE IF NOT EXISTS ADMINS (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
name TEXT NOT NULL,
rank TEXT,
done INTEGER,
created INTEGER
)
''')
def cleanup(all):
    d=[',',')',"'",'[',']','(']
    for i in d:
            result=all.replace(i,'')
    return result
def adduser(message):
    try:
        connection2=sqlite3.connect('admins.db',check_same_thread=False)
        cursor2 = connection2.cursor()
        info = cursor2.execute('SELECT * FROM ADMINS WHERE username=?', (message.from_user.username, )).fetchone()
        if info is None:
            cursor2.execute('INSERT INTO ADMINS (username,name,rank) VALUES (?,?,?)', (message.from_user.username,message.text,'user',))
            connection2.commit()
            connection2.close()
            bot.send_message(message.chat.id,'Успешно зарегестрирован.')
        elif len(info)==0:
            cursor2.execute('INSERT INTO ADMINS (username,name,rank) VALUES (?,?,?)', (message.from_user.username,message.text,'user',))
            connection2.commit()
            connection2.close()
            bot.send_message(message.chat.id,'Успешно зарегестрирован.')
        else:
            bot.send_message(message.chat.id,'Вы уже являетесь пользователем.')
    except ValueError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()
    except TypeError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()
    except sqlite3.IntegrityError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()


    
def addadmin(message):
    try:
        connection2=sqlite3.connect('admins.db',check_same_thread=False)
        cursor2 = connection2.cursor()#курсор
        info = cursor2.execute('SELECT * FROM ADMINS WHERE username=?', (message.from_user.username, )).fetchone()
        if info is None:
            bot.send_message(message.chat.id,'Вы не являетесь пользователем.')
        elif len(info)==0:
            bot.send_message(message.chat.id,'Вы не являетесь пользователем.')
        else:
            dds=message.from_user.username
            cursor2.execute('UPDATE ADMINS SET rank = "admin" WHERE username=?',(dds,))
            keyboard = types.ReplyKeyboardMarkup(row_width=3)#тип клавы, ширина
            keyboard.add(admin1,admin2,admin3,admin4,admin5,admin6)
            bot.reply_to(message,'Роль пользователя '+str(cleanup(message.from_user.username))+' Обновлена на Администратора.',reply_markup=keyboard)
            connection2.commit()
            connection2.close()
    except ValueError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()
    except TypeError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        cursor2.execute('INSERT INTO ADMINS (username) VALUES (?)', ('blank',))#КОСТЫЛИЩЕ, без него пустая бд не будет принимать
        connection2.commit()
        connection2.close()
    except sqlite3.IntegrityError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()



def checkadmin(message):
    try:
        asd='0'
        bsd='1'
        connection2=sqlite3.connect('admins.db',check_same_thread=False)
        cursor2 = connection2.cursor()#курсор
        info = cursor2.execute('SELECT * FROM ADMINS WHERE rank="admin" AND username=? ', (message.from_user.username, )).fetchone()
        if info is None:
            connection2.commit()
            connection2.close()
            return asd
        elif len(info)==0:
            connection2.commit()
            connection2.close()
            return asd
        else:
            return bsd
    except ValueError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()
    except TypeError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()
    except sqlite3.IntegrityError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error))
        connection2.commit()
        connection2.close()

def checkpassword(message):
    if message.text=='1978':
        addadmin(message)
    else:
        img = open('bin/notpass.gif', 'rb')
        bot.send_document(message.chat.id, img, None, '')
        img.close()

def addnote(message):#добавление задач, пишет ник, время и само задние
    try:
        connection = sqlite3.connect('tasks.db',check_same_thread=False)
        cursor = connection.cursor()
        abb=message.text
        ab=abb.split('/')
        date = datetime.now()#Пишет время, в функции так как вне ее пишет не настоящее на момент записи, а время запуска бота
        cursor.execute('INSERT INTO TASKS (time,task,username,anwser) VALUES (?,?,?,?)', (date,ab[0],message.from_user.username,ab[1],))
        #добавление данных
        connection.commit()#сохранияем
        connection.close()
        bot.send_message(message.chat.id, 'Добавлено задание:'+' '+str(ab[0]))#тот самый костыль
        connection2=sqlite3.connect('admins.db',check_same_thread=False)
        cursor2 = connection2.cursor()#курсор
        acc=cursor2.execute('SELECT created FROM ADMINS WHERE username=?',(message.from_user.username,)).fetchone()
        acc=cleanup(str(acc[0]))
        acc=acc.replace(',','')
        acc=acc.replace(')','')
        if acc == 'None':
            acc=1
            print(acc)
            dss=message.from_user.username
            sql='UPDATE ADMINS SET created = ? WHERE username=?'
            dql=(acc,dss,)
            cursor2.execute(sql,dql)
            connection2.commit()
            connection2.close()
        else:
            acc=cleanup(acc)
            acc=int(acc)+1
            acc=str(acc)
            print(acc)
            dss=message.from_user.username
            sql='UPDATE ADMINS SET created = ? WHERE username=?'
            dql=(acc,dss,)
            cursor2.execute(sql,dql)
            connection2.commit()
            connection2.close()
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
    except AttributeError as error:
        bot.send_message(message.chat.id,'Ты такого не отправляй, полжалуйста.')
        connection.commit()
        connection.close()
    except IndexError as error:
        bot.send_message(message.chat.id,'Ошибка при работе:  '+str(error)+'. Вы забыли дефис!')
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
        daymnedan(message)#тот самый 


def deleter(message):
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

def removefromexistence(message):
    connection2=sqlite3.connect('admins.db',check_same_thread=False)
    cursor2 = connection2.cursor()#курсор
    info = cursor2.execute('DELETE FROM ADMINS WHERE id < 10000000000')
    bot.send_message(message.chat.id,'Все пользователи удалены.')
    connection2.commit()
    connection2.close()
    

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()