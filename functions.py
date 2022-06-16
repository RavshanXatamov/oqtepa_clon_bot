from telegram import Update
from telegram.ext import CallbackContext
from buttons import *
from database import *
from random import choice

def start(update: Update, context: CallbackContext):
    update.message.reply_text("""
Ro'yxatdan o'tish uchun telefon raqqmingizni kiriting

Raqam +998********* shaqklida yuborilsin
    """, reply_markup=phone_buttons())
    return 'state_phone'


def command_phone(update: Update, context: CallbackContext):
    try:
        contact = update.message.contact
        phone_number = contact.phone_number
        context.user_data['phone_number'] = phone_number

    except Exception as e:
        phone = update.message.text
        if (phone[0] == '+' and len(phone) == 13 and phone[1:4] == '998') or (
                phone[:3] == '998' and len(phone) == 12) or (len(phone) == 9):
            phone_number = phone
            context.user_data['phone_number'] = phone_number

        else:
            update.message.reply_text("Siz telefon raqamingizni xato kiritdingiz yoki o'zbek raqam kiritmadingiz\n"
                                      "Qayta kiritib ko'ring:")
            return 'state_phone'

    update.message.reply_text(f"""
Sizning telefon raqamingiz
{context.user_data['phone_number']}
Sizga kim deb murojat qilaylik
Shu sababli isim yoki(va) familiyangizni yuboring

Masalan:Karimov Alisher
""")
    return 'state_name'


def command_name(update: Update, context: CallbackContext):
    number = choice(range(10000, 100000))
    context.user_data['code_id'] = number
    print(context.user_data['code_id'])
    context.user_data['name'] = update.message.text
    update.message.reply_text(f"""
{context.user_data['name']} sizga shu raqamni {number}
maxsus kod sifatida yubordik va siz bu 
siz bu kodni tasdiqlash uchun qayta jo'nating """)
    return 'state_login'


def command_permission(update: Update, context: CallbackContext):
    kod = update.message.text
    if int(kod) == context.user_data['code_id']:
        update.message.reply_photo(open("Image_story/main_image.jpg", "rb"),caption=f"Siz jo'natgan kod muvaffaqiyatli tasdiqlandi Asosiy sahifamizga xush kelibsiz", parse_mode="HTML",reply_markup=primary_buttons())
        return 'state_main'
    else:
        update.message.reply_text("Siz tasdiqlash kodini xato kitdingiz yana qata kiritib ko'ring")
        return "state_login"


def command_category(update: Update, context: CallbackContext):
    query=update.callback_query
    data=query.data
    query.message.delete()
    if data=='menu':
        query.message.reply_text("Buyurtmani birga joylashtiramizmi? 🤗",reply_markup=get_all_categories())
        return 'state_submain'
    elif data=='setting':
        query.message.reply_text(text="O'zigizga qulay bo'lgan tilini tanlang ",reply_markup=setting_button())
        return 'state_change_language'
    elif data=='carrier':
        query.message.reply_text(text="HR hizmatimiz bilan bo'lnishingiz uchun ************ raqmga tel qiling")
        return 'state_hr_department'

def command_products(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    query.message.delete()
    if data=='history':
        return 'state_history'
    elif data=='go_basket':
        return 'state_basket'
    elif data.isdigit():
        context.user_data['cat_id'] = data
        context.user_data['son'] = ''
        query.message.reply_photo(open("Image_story/lavash_category.jpg", "rb"),caption=f"Bo'lim lavashlar" ,reply_markup=get_all_product_bycat_id(int(context.user_data['cat_id'])))
        return 'state_product'

def command_product(update : Update,context: CallbackContext):
    query=update.callback_query
    data=query.data
    query.message.delete()
    context.user_data['data']=data
    if data.isdigit():
        context.user_data['product_id']=data
        query.message.reply_photo(open("Image_story/lavash_category.jpg", "rb"),caption="Assalom alaykum",reply_markup=get_order())
        return 'state_ordering'

    elif data == 'stored_item':
        pass
        return 'state_basket'

    elif data=='back':
        return 'state_submain'


def command_ordering(update: Update, context: CallbackContext):
    query = update.callback_query
    data =query.data

    if data.isdigit():
        son = '0'
        if context.user_data['son'] == '0':
            if context.user_data['son'] == '0':
                context.user_data['0'] = ''
            son = context.user_data['son'] + data
            context.user_data['son'] = son

        elif data != '0' and not (context.user_data['son']):
            son = data
            son += context.user_data['son']
            context.user_data['son']=son
            query.message.reply_text('Calculation process', reply_markup=get_ordering(context.user_data['son']))
    elif data=='delete':
        son=context.user_data['son']
        context.user_data['son']=son[:-1]
    elif data=='go_tobasket':
        return 'state_basket'
    elif data=='back':
        return 'state_submain'

def command_history(update : Update,context: CallbackContext):
    pass
def command_basket(update : Update, context : CallbackContext):
    query=update.callback_query
    data=query.data
    product=get_ordering(1)
    query.message.reply_photo(open("Image_story/lavash_category.jpg", "rb"),caption=f"{product[2]}\n"
                                                                                    f"narx :{product[3]}\n"
                                                                                    f"miqdor : {product[4]*product[3]}",reply_markup=basket_button())


