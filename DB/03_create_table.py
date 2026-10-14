cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    qualiti TNT ,
    price DECINAL,
    sale_date DATE
)
""")
