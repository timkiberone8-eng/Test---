import psycopg2

connection = psycopg2.connect(
    dname ="postgres",
    user ="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

connection.au = True

cursor = connection.cursor()

print("Подключение к базе postgres есть")

cursor.close()
connection.close()
