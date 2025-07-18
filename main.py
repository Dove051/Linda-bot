from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive

TOKEN = "7346331521:AAGyl4-S2ZjhA7gaotTkNKylSIx3pfYLQLk"
ADSTERRA_LINK = "https://ghettoformed.com/m9vn37uaan?key=a7cb844984d50bb7c45df57770b8fa69"

# Create unlock keyboard
def get_unlock_button():
    keyboard = [[InlineKeyboardButton("🔓 Tap Here to Unlock", url=ADSTERRA_LINK)]]
    return InlineKeyboardMarkup(keyboard)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to Linda’s Secret Vault 🔥\n\n"
        "You’re one step away from unlocking exclusive drops.",
        reply_markup=get_unlock_button()
    )

# Reply to any message
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👀 Still waiting? Tap below to unlock now!",
        reply_markup=get_unlock_button()
    )

# Set up the bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Keep alive + run
keep_alive()
app.run_polling()
