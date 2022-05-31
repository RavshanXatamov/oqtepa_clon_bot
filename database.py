from sqlite3 import connect

def create_table_users():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY UNIQUE ,
    telegram_id INTEGER , 
    full_name VARCHAR (185), 
    first_name VARCHAR (125), 
    phone VARCHAR (20)
    )
    """)

    conn.commit()

def create_table_category():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS categoties (
      id INTEGER PRIMARY KEY UNIQUE ,
      category_name VARCHAR (125)
      )
      """)

    conn.commit()


def create_table_products():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS products (
      product_id INTEGER PRIMARY KEY UNIQUE ,
      category_id INTEGER,
      product_name VARCHAR (125),
      unit_price INTEGER      )
      """)

    conn.commit()

def get_table_categories():
    conn = connect('main.db')
    cursor = conn.cursor()

    cursor.execute("""
    select * from categories    
    """)
    data = cursor.fetchall()
    return data

def get_table_products():
    conn = connect('main.db')
    cursor = conn.cursor()

    cursor.execute("""
    select * from categories    
    """)
    data = cursor.fetchall()
    return data