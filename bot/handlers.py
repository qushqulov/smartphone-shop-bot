from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from bot.database import db


def start_command(update: Update, context: CallbackContext):
    user = update.effective_user

    db.add_user(user_id=user.id, first_name=user.first_name)

    update.message.reply_text(
        text=f"Assalomu alaykum {user.first_name}!\n\nSmartphone Shop Botga xush kelibsiz!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton("Telefonlar"), KeyboardButton("Haridlarim")]]
        ),
    )


def send_smartphones_handler(update: Update, context: CallbackContext):
    pass
