import telebot,sqlite3
from cfg import token
ada=None
bot = telebot.TeleBot(token)
def cleanup(all):
    d=[',',')',"'",'[',']','(']
    for i in d:
            result=all.replace(i,'')

def daymnedan(message):
    if (message.text.isdigit()):
        connection = sqlite3.connect('tasks.db',check_same_thread=False)
        cursor = connection.cursor()
        a=message.text
        d=[',',')',"'",'[',']','(',]
        resultid = str(cursor.execute("SELECT id FROM TASKS where id = "+str(a)).fetchall())
        resultname = str(cursor.execute("SELECT username FROM TASKS where id = "+str(a)).fetchall())
        resulttime = str(cursor.execute("SELECT time FROM TASKS where id = "+str(a)).fetchall())
        resulttask = str(cursor.execute("SELECT task FROM TASKS where id = "+str(a)).fetchall())
        print(a)
        for i in d:
            resultid=resultid.replace(i,'')
            resultname=resultname.replace(i,'')
            resulttime=resulttime.replace(i,'')
            resulttask=resulttask.replace(i,'')
        id=resultid
        name=resultname
        time=resulttime
        task=resulttask
        bot.send_message(message.chat.id,'Айди: '+str(id)+"\n"+'Имя пользователя: '+str(name)+"\n"+'Время создания задания: '+str(time)+"\n"+'Задача: '+str(task))
        connection.commit()
        connection.close()
    else:
        bot.send_message(message.chat.id, 'Брат, это явно не число.')


    
def lichnoe(message):
        connection2 = sqlite3.connect('admins.db',check_same_thread=False)
        cursor2 = connection2.cursor()
        a=message.from_user.username
        d=[',',')',"'",'[',']','(',]
        resultname = str(cursor2.execute("SELECT username FROM ADMINS where username = ?",(str(a),)).fetchall())
        resultrank = str(cursor2.execute("SELECT rank FROM ADMINS where username = ?",(str(a),)).fetchall())
        resultdone = str(cursor2.execute("SELECT done FROM ADMINS where username = ?",(str(a),)).fetchall())
        resultcreated = str(cursor2.execute("SELECT created FROM ADMINS where username = ?",(str(a),)).fetchall())
        print(a)
        for i in d:
            resultname=resultname.replace(i,'')
            resultrank=resultrank.replace(i,'')
            resultdone=resultdone.replace(i,'')
            resultcreated=resultcreated.replace(i,'')
        bot.send_message(message.chat.id,'Имя пользователя: '+str(resultname)+"\n"+'Статус: '+str(resultrank)+"\n"+'Выполнено задач: '+str(resultdone)+"\n"+'Создано задач: '+str(resultcreated))
        connection2.commit()
        connection2.close()
