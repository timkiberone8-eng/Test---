cursor.execute("DELETE FROM sales")
sales_data = [
    ("laptop",10,700,datetime(2024,1,10)),
    ("Smartphone",25,300,datetime(2024,1,11))
    ("Tablet",15,250,datetime(2024,1,12))
    ("Headphones",50,50,datime(2024,1,13))
    ("Smartwatch",30,150,datetime(2024,1,14)),
]


for sale in sales_data:
    cursor.execute("INSENT INTO sales (producr_name,quality,price" \
    "sale_date) VALUES ")

connection commit()
print("Данные добавлены")

cursor.close()
connection.close()
