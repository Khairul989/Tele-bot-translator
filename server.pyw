from telegram.ext import *
from telegram import *
import gizoogle

bots = Bot("1280697835:AAHFFEkFu20QdxvCP40IpUsQXa4Hm6qIAgE")
print(bots)

updater = Updater("1280697835:AAHFFEkFu20QdxvCP40IpUsQXa4Hm6qIAgE", use_context=True)

dispatcher: Dispatcher = updater.dispatcher


def sendback(update: Update, context: CallbackContext):
    global msg, chat_id

    msg = update.message.text
    chat_id = update.message.chat_id
    usern = update.message.chat.username

    reply = gizoogle.translateText(msg, usern)

    bots.send_message(chat_id=chat_id,
                      text=reply,
                      parse_mode=ParseMode.HTML)


dispatcher.add_handler(MessageHandler(Filters.text, sendback))
updater.start_polling()
