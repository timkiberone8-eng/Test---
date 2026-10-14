import psycopg2

connection = psycopg2.connect(
    dbname ="postgres",
    user ="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

connection.autocommit = True

cursor = connection.cursor()

print("Подключение к базе postgres есть")

cursor.close()
connection.close()
