from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler, 
    Filters         
)

from bot.config import settings
from bot.handlers import (
    start_command,
    send_smartphones_handler,
    show_models_handler, 
)

def main():
    updater = Updater(settings.BOT_TOKEN)
    dp = updater.dispatcher

   
    dp.add_handler(CommandHandler("start", start_command))

    
    dp.add_handler(MessageHandler(Filters.regex('^Telefonlar$'), send_smartphones_handler))

    
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, show_models_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()