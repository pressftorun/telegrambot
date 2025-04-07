from cfg import token#импорт кода других папок и модулей
import telebot,sqlite3
from needdisp import *
ada=None
from sqlite3 import Error
from sqlite import *
from buttons import button1, button2, button3,button4,button5,button6,button7,button8,button9
from telebot import types
bot = telebot.TeleBot(token)#токен бота,ВАЖНО!
@bot.message_handler(commands = ['start'])#команда старт(по коду, то что после собаки-условие, вызывающее функцию под ним)
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3)#тип клавы, ширина
    keyboard.add(button1, button2, button3,button4,button5,button6,button7,button8,button9)
    bot.reply_to(message, 'Приветствую вас, этот бот создан для обучения сотрудников в игровой форме с заданиями. Тут вы можете выполнять и просматиривать задания.', reply_markup=keyboard)#непосредственно добавляет клаву
    bot.send_message(message.chat.id, 'Введите ваше имя:')
    bot.register_next_step_handler(message,adduser)
@bot.message_handler(commands = ['help'])
def helpfunc(message):
    bot.send_message(message.chat.id, 'Привет, напиши слово СЕГОДНЯ, ЗАВТРА или ВЧЕРА')

@bot.message_handler(commands = ['lk'])
def helpfunc(message):
    lichnoe(message)
    
@bot.message_handler(commands = ['dotask'])
def dotask(message):
    bot.send_message(message.chat.id, 'Введите номер задания из списка для выполнения: '+str(getnumbers()))
    bot.register_next_step_handler(message,dotaska)

@bot.message_handler(commands = ['checktasks'])
def helpfunc(message):
    bot.send_message(message.chat.id, 'Введите номер задания из списка для просмотра: '+str(getnumbers()))
    bot.register_next_step_handler(message,giveinf)


@bot.message_handler(commands = ['addtask'])
def helpfunc(message):
    if checkadmin(message)=='1':
        bot.send_message(message.chat.id, 'Введите задание и ответ на него через /')
        bot.register_next_step_handler(message,addnote)#тут у нас отсылка сообщения в файле sqlite, потом ответ отттуда же(костыль)
    else:
        bot.send_message(message.chat.id, 'Нет доступа')
        


@bot.message_handler(commands = ['deltask'])
def delfunc(message):
    if checkadmin(message)=='1':
        bot.send_message(message.chat.id, 'Введите номер задания для удаления')
        bot.register_next_step_handler(message,deleteinf)
    else:
        bot.send_message(message.chat.id, 'Нет доступа')

@bot.message_handler(commands = ['addadmin'])
def addadminbot(message):
    addadmin(message)
@bot.message_handler(commands = ['removeusers'])
def reference(message):
    removefromexistence(message)


def dotaska(message):
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM TASKS")#выбирает все
    a=cursor.fetchall()#выбирает все
    connection.commit()
    b=len(a)
    if b==0:
        bot.send_message(message.chat.id,'Нету записей в базе данных')
    else:
        dantask(message)#тот самый

def dantask(message):
    if (message.text.isdigit()):
        connection = sqlite3.connect('tasks.db',check_same_thread=False)
        cursor = connection.cursor()
        global ada,gda
        gda=message
        ada=message.text
        d=[',',')',"'",'[',']','(',]
        resulttask = str(cursor.execute("SELECT task FROM TASKS where id = "+str(ada)).fetchall())
        print(ada)
        for i in d:
            resulttask=resulttask.replace(i,'')
        task=resulttask
        connection.commit()
        connection.close()
        def helpmealready(message):
            msg=bot.reply_to(message,'Задача: '+str(task)+';'+'Напишите свой ответ')
            bot.register_next_step_handler(msg,checkanwser)
        helpmealready(message)
        print('+')
    else:
        bot.send_message(message.chat.id, 'Брат, это явно не число.')
def checkanwser(message):
    connection = sqlite3.connect('tasks.db',check_same_thread=False)
    d=[',',')',"'",'[',']','(',]
    print('cheackasdas')
    cursor = connection.cursor()
    connection2 = sqlite3.connect('admins.db',check_same_thread=False)
    cursor2 = connection2.cursor()
    g=message.from_user.username
    a=ada
    resultanwser = str(cursor.execute("SELECT anwser FROM TASKS where id = "+str(a)).fetchall())
    for i in d:
        resultanwser=resultanwser.replace(i,'')
    b=message.text
    b=b.lower()
    if b==resultanwser.lower():
        bot.send_message(message.chat.id,'Ответ верен')
        acc=cursor2.execute('SELECT done FROM ADMINS WHERE username=?',(message.from_user.username,)).fetchone()
        acc=cleanup(str(acc[0]))
        acc=acc.replace(',','')
        acc=acc.replace(')','')
        deleter(gda)
        if acc == 'None':
            acc=1
            print(acc)
            dss=message.from_user.username
            sql='UPDATE ADMINS SET done = ? WHERE username=?'
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
            sql='UPDATE ADMINS SET done = ? WHERE username=?'
            dql=(acc,dss,)
            cursor2.execute(sql,dql)
            connection2.commit()
            connection2.close()
    else:
        bot.send_message(message.chat.id,'Ответ неверен')
    
#принимает сообщения на постоянке, если нет обращения к командам типа /...(СТАВИТЬ В САМЫЙ НИЗ)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'Чет не то ты написал...')


bot.polling(none_stop = True)#цикл работы бота(чтоб не отключался(он отключится после 5 минут афк где-то))
