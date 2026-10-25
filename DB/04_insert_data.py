import psycopg2
from datetime import datetime


connection = psycopg2.connect(
    dbname ="",
    user ="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

cursor = connection.cursor()
cursor.execute("DELETE FROM sales")
sales_data = [
    ("СОК",10,700,"2026-10,200")
    ("Вода",25,300,"2026-10,200")
    ("СОК",15,250,"2026-10,200")
    ("Сэндвич",50,50,"2026-10,200")
    ("Вода",30,150,"2026-10,200")
    ("СОК",15,250,"2026-10,200")
]
cursor = connection.cursor()

cursor.execute("""
"""
for sale in sales_data:
    cursor.execute("INSERT INTO sales (product_name,quantity,price," \
    "sale_date) VALUES (%s, %s, %s, %s)", sale)

connection.commit()
print("Данные добавлены")

cursor.close()
connection.close()