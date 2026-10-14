import psycopg2

connection = psycopg2.connect(
    dbname ="sales_data",
    user ="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432",
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT ,
    price DECIMAL,
    sale_date DATE
)
""")

connection.commit()
print("Таблица создана")

cursor.close()
connection.close()
