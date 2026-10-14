import json
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# --- Getting bot and user data from json file ---

DATA_FILE = "data.json"

with open(DATA_FILE, "r") as data:
    imported_data = json.load(data)
    BOT_TOKEN = imported_data["bot_token"]
    USER_ID = imported_data["user_id"]

# --- functions that handle commands ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is working!")

# --- main function ---

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

# --- Run the script ---

if __name__ == "__main__":
    main()