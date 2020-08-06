from telegram.ext import *
from telegram import *

bot = Bot("1240293750:AAFSL_ISptGUT4tRJf0DaYqSnsZqGeNv0hY")
print(bot.getMe())

updater = Updater("1240293750:AAFSL_ISptGUT4tRJf0DaYqSnsZqGeNv0hY",use_context=True)

dispatcher : Dispatcher = updater.dispatcher

def test(update:Update, context:CallbackContext):
    bot.send_message(chat_id=update.effective_chat.id,
                     text= 'Working',
                     parse_mode=ParseMode.HTML)


dispatcher.add_handler(MessageHandler(Filters.text,test1))
updater.start_polling()