from telegram.ext import Updater, MessageHandler,Filters,  CommandHandler,CallbackQueryHandler,  CallbackContext, ConversationHandler
from telegram import Update
from functions import *

conversation_handler=ConversationHandler(

    entry_points=[
        CommandHandler('start',start)
    ],
    states={
        'state_phone' : [
            CommandHandler('start',start),
            MessageHandler(Filters.text,command_phone),
            MessageHandler(Filters.contact,command_phone)
        ],
        'state_name' : [
            CommandHandler('start', start),
            MessageHandler(Filters.text,command_name)
        ],
        'state_login' : [
            CallbackQueryHandler(command_permission),
            MessageHandler(Filters.text,command_permission)
        ],
        'state_main' : [
            CallbackQueryHandler(command_category)
        ],
        'state_submain' : [
            CallbackQueryHandler(command_products)
        ],
        'state_product' : [
            CallbackQueryHandler(command_product)
        ]
    },

    fallbacks=[
        CommandHandler('start',start)
    ]
)
updater = Updater("5237577605:AAH28vC-vcOps0Wlyh2TIFkAo49d3672Wak")
updater.dispatcher.add_handler(conversation_handler)
updater.start_polling()
updater.idle()



# for github
# git remote add origin <github link>
# git push origin <branch : master,main  >
# colorhunt.co
