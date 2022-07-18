import goer
import fetchProfile
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.environ['TELEGRAM_TOKEN']


async def go(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = fetchProfile.get_image_by_username(update.message.text.split()[-1])
    file = goer.get_goed_image(file)
    await update.message.reply_photo(file)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("go", go))

app.run_polling()
