import sqlite3
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
print(cleanstr)