import psycopg2
from datetime import datetime

import psycodg2
import math

connection = psycopg2.connect(
    dbname ="sales_data",
    user ="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

cursor = connection.cursor()
cursor.execute 
SELECT sale_date, SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY sale_date
ORDER BY sale_date

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

pit.figure(figsize={10, 6})
pit.bar(products,revenue , color="blue",alpha = 0.7)
pit.title("Общая выручка из продукии")
pit.xlabe[("Продукция")]
pit.ylabel[("Выручка")]
pit.show()