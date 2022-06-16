from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from database import *

def phone_buttons():
    button = [
        [KeyboardButton('raqamni yuborish', request_contact=True)]
    ]
    return ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)

def primary_buttons():
    button = []
    res = []
    res.append(InlineKeyboardButton("Carrier", callback_data='carrier'))
    res.append(InlineKeyboardButton("Setting", callback_data='setting'))
    button.append([InlineKeyboardButton("Menu", callback_data='menu')])
    button.append(res)
    return InlineKeyboardMarkup(button)


def get_all_categories():
    res = []
    button = []
    data = get_table_categories()
    for category in data:
        res.append(InlineKeyboardButton(category[1], callback_data=category[0]))
        if len(res) == 2:
            button.append(res)
            res = []

    if len(res) > 0:
        button.append(res)
        res=[]
    button.append([InlineKeyboardButton(text="Buyurtmalar tarixi", callback_data="history")])
    button.append([InlineKeyboardButton(text="Savatchaga o'tish", callback_data="go_basket")])

    return InlineKeyboardMarkup(button)

def get_all_product_bycat_id(id_bycat):
    category=get_table_products(cat_id=id_bycat)
    res = []
    button = []

    for product in category:
        res.append(InlineKeyboardButton(product[2], callback_data=product[0]))
        if len(res) == 2:
            button.append(res)
            res = []
    if len(res) > 0:
        button.append(res)
    button.append([InlineKeyboardButton(text="Savatchaga qo'shish", callback_data="stored_item")])
    button.append([InlineKeyboardButton(text="Orqaga", callback_data="back")])

    return InlineKeyboardMarkup(button)

def get_ordering(son):
    res=[]
    button=[]
    button.append([InlineKeyboardButton(f"Tanlanganlar {son}",callback_data='order_number')])
    for i in range(1,10):
        res.append(InlineKeyboardButton(f"{i}",callback_data=f"{i}"))
        if len(res)==3:
            button.append(res)
            res=[]
    res.append(InlineKeyboardButton(f"{son}",callback_data=f"{0}"))
    res.append(InlineKeyboardButton(f"O'chirish",callback_data='delete'))
    button.append(res)
    button.append([InlineKeyboardButton("Savatchaga qo'shish",callback_data="go_tobasket")])
    button.append([InlineKeyboardButton("Orqaga",callback_data='back')])

    return InlineKeyboardMarkup(button)



def get_order():
    res=[]
    button=[]
    son=0
    button.append([InlineKeyboardButton(f"Tanlanganlar {son}",callback_data='order_number')])
    for i in range(1,10):
        res.append(InlineKeyboardButton(f"{i}",callback_data=f"{i}"))
        if len(res)==3:
            button.append(res)
            res=[]
    res.append(InlineKeyboardButton(f"{son}",callback_data=f"{0}"))
    res.append(InlineKeyboardButton(f"O'chirish",callback_data='delete'))
    button.append(res)
    button.append([InlineKeyboardButton("Savatchaga qo'shish",callback_data="go_tobasket")])
    button.append([InlineKeyboardButton("Orqaga",callback_data='back')])

    return InlineKeyboardMarkup(button)
def setting_button():
    res=[]
    button=[]
    res.append(InlineKeyboardButton("English",callback_data='english'))
    res.append(InlineKeyboardButton("Russian",callback_data='russia'))
    button.append(res)
    button.append([InlineKeyboardButton("Uzbek",callback_data='uzbek')])

    return InlineKeyboardMarkup(button)

def basket_button():
    res=[]
    button=[]
    order_conditation=get_order_details(telegram_id)
    res.append(InlineKeyboardButton('-',callback_data='minus'))
    res.append(InlineKeyboardButton(f"{order_conditation[2]}"))
    res.append(InlineKeyboardButton('+',callback_data='plus'))
    button.append(res)
    button.append([InlineKeyboardButton('Buyurtmani tasdiqlash',callback_data='booking')])
    button.append([InlineKeyboardButton('Orqaga',callback_data='back')])
    return InlineKeyboardMarkup(button)









