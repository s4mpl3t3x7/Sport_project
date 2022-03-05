import pandas as pd
import pymysql.cursors
import matplotlib.pyplot as plt
# Подключение к базе данных:
connection = pymysql.connect(host = '127.0.0.1',
user = 'root',
password = 'admin',
db ='social_network',
charset ='utf8mb4',
cursorclass = pymysql.cursors.DictCursor)
with connection.cursor() as cursor:
    sql = "SELECT * FROM communities " # запрос SQL
    cursor.execute(sql) # Выполнение команды запроса 
    rows = cursor.fetchall()# получение всех строчек
    df = pd.DataFrame(rows) # получение таблицы с данными
    sql = "SELECT comName, ComNumUsers FROM communities ORDER BY ComNumUsers DESC LIMIT 5;" 
    cursor.execute(sql)
    rows = cursor.fetchall()
    df2 = pd.DataFrame(rows) 
    sql = "SELECT JobName, JobPositions FROM jobs where JobPositions > 5;" 
    cursor.execute(sql)
    rows = cursor.fetchall()
    df3 = pd.DataFrame(rows)
    sql = "SELECT Sex, SUM(Height) as Sum FROM profile group by sex;" 
    cursor.execute(sql)
    rows = cursor.fetchall()
    df4 = pd.DataFrame(rows) 
    connection.close() # Закрытие соединения (Close connection).
print(df, "\n")
print(df2, "\n")
print(df3, "\n")
print(df4, "\n")
# Построение графиков:
"""
plt.figure()
plt.tick_params(axis='x',rotation=90) # поворот подписи по оси х на 90 градусов
plt.bar(df2['comName'],df2['ComNumUsers']) # гистограмма
plt.legend(['Количество'])
plt.title('Топ 5 сообществ по количеству пользователей')
plt.xlabel('Сообщество')
plt.ylabel('Количество пользователей')
plt.show() # вывод гистограммы

plt.figure()
plt.tick_params(axis='x',rotation=90)
plt.barh(df3['JobName'],df3['JobPositions'], color='red') 
plt.legend(['Количество вакансий'])
plt.title('Профессии с более, чем 5 вакансиями')
plt.xlabel('Количество вакансий')
plt.ylabel('Профессии')
plt.show()
"""
plt.figure()
plt.tick_params(axis='x',rotation=90)
clr = ['r','b']
plt.pie(df4['Sum'],labels=df4['Sex'],colors=clr,autopct='%1.1f%%') #pie chart
plt.legend(['Вес женщин', 'Вес мужчин'])
plt.title('Соотношение суммарного веса пользователей по полу')
plt.show()
