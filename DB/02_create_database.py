cursor = execute("DROP DATABASE IF EXISTS sales_data")
cursor = execute("CREATE DATABASE sales_data")
print("База данных создана")

cursor.close()
connection.close()
