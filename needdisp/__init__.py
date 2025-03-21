import telebot,sqlite3
from cfg import token
bot = telebot.TeleBot(token)
def daymnedan(message):
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    cursor = connection.cursor()
    a=message.text
    print(a)
    resultid = str(cursor.execute("SELECT id FROM TASKS where id = "+str(a)).fetchall())
    resultid1=resultid.replace(',','')
    resultid2=resultid1.replace(')','')
    resultid3=resultid2.replace("'",'')
    resultid4=resultid3.replace('[','')
    resultid5=resultid4.replace(']','')
    resultid6=resultid5.replace('(','')
    id=resultid6
    resultname = str(cursor.execute("SELECT username FROM TASKS where id = "+str(a)).fetchall())
    resultname1=resultname.replace(',','')
    resultname2=resultname1.replace(')','')
    resultname3=resultname2.replace("'",'')
    resultname4=resultname3.replace('[','')
    resultname5=resultname4.replace(']','')
    resultname6=resultname5.replace('(','')
    name=resultname6
    resulttime = str(cursor.execute("SELECT time FROM TASKS where id = "+str(a)).fetchall())
    resulttime1=resulttime.replace(',','')
    resulttime2=resulttime1.replace(')','')
    resulttime3=resulttime2.replace("'",'')
    resulttime4=resulttime3.replace('[','')
    resulttime5=resulttime4.replace(']','')
    resulttime6=resulttime5.replace('(','')
    timecreated=resulttime6
    resulttask = str(cursor.execute("SELECT task FROM TASKS where id = "+str(a)).fetchall())
    resulttask1=resulttask.replace(',','')
    resulttask2=resulttask1.replace(')','')
    resulttask3=resulttask2.replace("'",'')
    resulttask4=resulttask3.replace('[','')
    resulttask5=resulttask4.replace(']','')
    resulttask6=resulttask5.replace('(','')
    task=resulttask6
    bot.send_message(message.chat.id,'Айди: '+str(id)+"\n"+'Имя пользователя: '+str(name)+"\n"+'Время создания задания: '+str(timecreated)+"\n"+'Задача: '+str(task))
    connection.commit()
    connection.close()