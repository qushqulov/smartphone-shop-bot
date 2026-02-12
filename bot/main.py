from telegram.ext import (
    Updater,
    CommandHandler,
)

from bot.config import settings
from bot.handlers import (
    start_command,
    send_smartphones_handler,
)


def main():
    updater = Updater(settings.BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("Telefonlar", send_smartphones_handler))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
