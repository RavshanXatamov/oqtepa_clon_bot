import sqlite3
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
    phone VARCHAR (20))
    """)

    conn.commit()

def create_table_category():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS categories (
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

def order_details():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS order_detail (
      order_id INTEGER PRIMARY KEY UNIQUE ,
      product_id INTEGER,
      product_name VARCHAR (125),
      unit_price INTEGER,
      quantity INTEGER,
      status VARCHAR (125))

      """)

    conn.commit()
    return 'it is done'

def create_user_table():
    conn=connect('main.db')
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS list_of_users (
    user_id INTEGER,
    user_name VARCHAR (150),
    user_full_name VARCHAR (200),
    user_phone_number VARCHAR (100),
    connection_number INTEGER)
    """)

    conn.commit()
    return 'it is done'

def get_table_categories():
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute("""
    select * from categories    
    """)
    data = cursor.fetchall()
    return data

def get_table_products(cat_id):
    conn = connect('main.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    select * from products 
    where category_id={cat_id}   
    """)
    data = cursor.fetchall()
    return data

# def put_info_into_userlist():
#     conn=connect('main.db')
#     cursor=conn.cursor()
#
#     cursor.execute("""
#     INSERT INTO list_of_users()
#     VALUES ()
#        """
#     conn.commit())
#     return 'it is done : '

def check_user(id):
    conn=connect('main.db')
    cursor=conn.cursor()
    cursor.execute(f"""
    select * from list_of_users
    where user_id={id}
    
    """)
    data=cursor.fetchone()
    if data:
        return True
    else:
        return data

def get_product_byproduct_id(id):
    conn=connect('main.db')
    cursor=conn.cursor()
    cursor.execute(f"""
    select * from products
    where product_id={id}
    """)
    data=cursor.fetchone()
    return data




def add_user(telegram_id, full_name, first_name, phone, viloyat):


    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO users (telegram_id, full_name, first_name, phone, viloyat)
    VALUES ({telegram_id}, "{full_name}", "{first_name}", '{phone}', "{viloyat}")
    """)
    conn.commit()


def get_order_details(telegram_id):
    conn = connect('main.db')
    cursor = conn.cursor()
    cursor.execute(f"""
       select * from order_details
       where telegram_id={telegram_id}
       """)
    data = cursor.fetchone()
    return data

def put_order_details(product_id,product_name,unit_price,quantity,status):
    conn=connect('main.db')
    cursor=conn.cursor()
    cursor.execute(f"""
    insert into order_detail (product_id,product_name,unit_price,quantity,status)
    values ({product_id},{product_name},{unit_price},{quantity},{status})
    """)

    conn.commit()