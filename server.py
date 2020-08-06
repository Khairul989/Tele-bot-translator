from telegram.ext import *
from telegram import *
import gizoogle

bots = Bot("1240293750:AAFSL_ISptGUT4tRJf0DaYqSnsZqGeNv0hY")
print(bots)

updater = Updater("1240293750:AAFSL_ISptGUT4tRJf0DaYqSnsZqGeNv0hY", use_context=True)

dispatcher: Dispatcher = updater.dispatcher


def sendback(update: Update, context: CallbackContext):
    global msg, chat_id

    msg = update.message.text
    chat_id = update.message.chat_id

    reply = gizoogle.translateText(msg)

    bots.send_message(chat_id=chat_id,
                      text=reply,
                      parse_mode=ParseMode.HTML)


dispatcher.add_handler(MessageHandler(Filters.text, sendback))
updater.start_polling()
