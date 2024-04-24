import json
import mysql.connector

def import_products():
    with open('petlebi_products.json', 'r') as file:
        data = json.load(file)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="db"
    )
    cursor = conn.cursor()

    create_petlebi_table(cursor)

    for product in data:
        insert_product(cursor, product)

    conn.commit()
    conn.close()

def create_petlebi_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS petlebi (
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_url VARCHAR(255),
            product_name VARCHAR(255),
            product_price VARCHAR(50),
            product_id VARCHAR(50),
            product_img VARCHAR(1000),
            barcode VARCHAR(50),
            brand VARCHAR(255),
            description TEXT
        )
    """)

def insert_product(cursor, product):
    cursor.execute("""
        INSERT INTO petlebi (
            product_url, 
            product_name, 
            product_price, 
            product_id, 
            product_img, 
            barcode, 
            brand, 
            description
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        product.get('product URL'),
        product.get('product name'),
        product.get('product price'),
        product.get('ID '),
        product.get('IMG '),
        product.get('barcode'),
        product.get('brand'),
        product.get('description')
    ))

    print(f"Inserted product: {product['product name']}")

if __name__ == "__main__":
    import_products()
