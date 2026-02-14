from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext
from bot.database import db

def start_command(update: Update, context: CallbackContext):
    user = update.effective_user
    db.add_user(user_id=user.id, first_name=user.first_name)

    update.message.reply_text(
        text=f"Assalomu alaykum {user.first_name}!\n\nSmartphone Shop Botga xush kelibsiz!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Telefonlar")],
                [KeyboardButton("Haridlarim")]
            ],
            resize_keyboard=True
        ),
    )

def send_smartphones_handler(update: Update, context: CallbackContext):
    
    smartphones = db.data.get("smartphones", {})
    
   
    brands = list(set(item["brand"] for item in smartphones.values()))
    
  
    keyboard = []
    for i in range(0, len(brands), 2):
        row = [KeyboardButton(brands[i])]
        if i + 1 < len(brands):
            row.append(KeyboardButton(brands[i+1]))
        keyboard.append(row)
    
   
    keyboard.append([KeyboardButton("Asosiy menyu")])

    update.message.reply_text(
        text="Brendni tanlang:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

def show_models_handler(update: Update, context: CallbackContext):
    text = update.message.text 
    smartphones = db.data.get("smartphones", {})
    
   
    models = []
    for key, details in smartphones.items():
        if details["brand"] == text:
            models.append(details["model"])
    
    if models:
        
        keyboard = [[KeyboardButton(m)] for m in models]
        keyboard.append([KeyboardButton("Telefonlar")]) 
        
        update.message.reply_text(
            text=f"{text} modellari:",
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )