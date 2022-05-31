from telegram import Update
from telegram.ext import CallbackContext
from buttons import *
from database import *

def start(update: Update, context: CallbackContext):
    # if check_user(update.effective_user.id):
    #     update.message.reply_text("Buyurtmani birga joylashtiramizmi? 🤗", reply_markup=get_all_category())
    #     return 'state_main'
    update.message.reply_text("""Ro'yxatdan o'tish uchun telefon
    raqamingizni kiriting
    
    Raqamni +998******* shaklida yuboring.""")
    return 'state_phone'

def command_phone(update: Update, context: CallbackContext):
    update.message.reply_text("""Sizga kim deb murojad qilaylik
    Shu sababli ism va familiyangizni yuboring 
    
    Masalan : Karimov Salim""")
    return 'state_name'

def command_name(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text("Sizning ismi familyangiz " + text + "\n"
                                                                   "Yaxshi endi telefon raqamingizni yuboring",
                              reply_markup=get_all_category())
    context.user_data['name'] = text
    return 'state_main'

def command_category(update:Update, context:CallbackContext):
    query = update.callback_query
    data = str(query.data)
    query.message.delete()
    if data.isdigit():
        cat_name = get_name_bycatid(int(data))[0]
        query.message.reply_photo(open('images.png', 'rb'), caption=f"Bo'lim", parse_mode='HTML')