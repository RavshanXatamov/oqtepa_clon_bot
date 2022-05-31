from telegram import  ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from database import *

def  get_all_category():
    res=[]
    button=[]
    admin_panel=[]
    data=get_table_category()
    for category in data:
        res.append(InlineKeyboardButton(category[1], callback_data=category[0]))
        if len(res)==2:
            button.append(res)
            res=[]
    if len(res)>0:
        button.append(res)
    button.append(InlineKeyboardButton('Buyurtmalar tarixi',callback_data='history'))
    button.append(InlineKeyboardButton("Savatchaga o'tish"))
    admin_panel.append(InlineKeyboardButton('Karyera',callback_data='karyera'))
    admin_panel.append(InlineKeyboardButton("Tilni o'zgartirish",callback_data='settings'))
    button.append(admin_panel)

    return InlineKeyboardMarkup(button)

def phone_button():
    button=[
        [KeyboardButton('raqamni yuborish',request_contact=True)]
    ]
    return ReplyKeyboardMarkup(button,resize_keyboard=True,one_time_keyboard=True)

def product_via_category_id():
    data=get_table_products()
    res=[]
    button=[]
    for product in data:
        res.append(InlineKeyboardButton(product[2],callback_data=product[1]))
        if len(res)==2:
            button.append(res)
            res=[]
    if len(res)>0:
        button.append(res)
    button.append(InlineKeyboardButton("savatga qo'shish",callback_data='savedlist'))
    button.append(InlineKeyboardButton("orqaga",callback_data='backward'))

    return InlineKeyboardMarkup(button)