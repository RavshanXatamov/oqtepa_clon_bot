from telegram.ext import Updater, MessageHandler,Filters,  CommandHandler,CallbackQueryHandler,  CallbackContext, ConversationHandler
from telegram import Update
import logging

from buttons import *
from functions import *
from database import *

conversation_handler=ConversationHandler(

    entry_points=[
        CommandHandler('start',start)
    ],
    states={
        'state_phone' : [
            CommandHandler('start',start),
            MessageHandler(Filters.text,command_phone)
        ],
        'state_name' : [
            CommandHandler('start', start),
            MessageHandler(Filters.text,commnand_phone)
        ],
        'state_main' : [
            CallbackQueryHandler(command_category)
        ]
    },

    fallbacks=[
        CommandHandler('start',start)
    ]
)

updater = Updater("5237577605:AAH28vC-vcOps0Wlyh2TIFkAo49d3672Wak")
updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()