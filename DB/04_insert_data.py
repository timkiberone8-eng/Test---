import psycopg2
from datetime import datetime

connection = psycopg2.connect(
    dbname ="sales_data",
    user ="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

cursor = connection.cursor()

cursor.execute("DELETE FROM sales")
sales_data = [
    ("laptop",10,700,datetime(2024,1,10)),
    ("Smartphone",25,300,datetime(2024,1,11)),
    ("Tablet",15,250,datetime(2024,1,12)),
    ("Headphones",50,50,datetime(2024,1,13)),
    ("Smartwatch",30,150,datetime(2024,1,14)),
]


for sale in sales_data:
    cursor.execute("INSERT INTO sales (product_name,quantity,price," \
    "sale_date) VALUES (%s, %s, %s, %s)", sale)

connection.commit()
print("Данные добавлены")

cursor.close()
connection.close()
