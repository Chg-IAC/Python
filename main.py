from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
token="1554953563:AAGU1A3b1lTrxERzRuJJAioyLZaGq-4QGTo"
message_bienvenue = "Service ouvert"
def message_begin(text):
    chat_id = "891168500"
    url_req = "https://api.telegram.org/bot"+token+"/sendMessage" + "?chat_id="+chat_id+"&text="+text
    results = requests.get(url_req)
#message_begin(message_bienvenue)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Bienvenue sur notre site de service')
    
 
def main():
    message_begin(message_bienvenue)
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main() 
    
