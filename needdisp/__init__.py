import telebot,sqlite3
from cfg import token
bot = telebot.TeleBot(token)
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