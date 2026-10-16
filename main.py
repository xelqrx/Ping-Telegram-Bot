import json
import asyncio
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from terminal_cmds import ping_site

# --- Getting bot and user data from json file ---

DATA_FILE = "data.json"

with open(DATA_FILE, "r") as data:
    imported_data = json.load(data)
    BOT_TOKEN = imported_data["bot_token"]
    USER_ID = imported_data["user_id"]
    TARGET = imported_data["target_ip"]

# --- functions that handle commands ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.delete()
    await update.message.reply_text("Hello!")

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == USER_ID:
        await update.message.reply_text("Pinging your router...")
        result = ping_site(TARGET, "1")
        if result == 0:
            await update.message.reply_text("Router is online! Lucky;)")
        else:
            await update.message.reply_text("Could not ping your router. Router is offline. What a shame:(")
    else:
        await update.message.reply_text("Hello!")

# --- main function ---

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("check", check))

    app.run_polling()

# --- Run the script ---

if __name__ == "__main__":
    main()