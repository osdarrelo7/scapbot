from telegram.ext import ApplicationBuilder, CommandHandler
import os

async def start(update, context):
    await update.message.reply_text("Hola, soy tu bot.")

if __name__ == '__main__':
    TOKEN = os.getenv("7352077618:AAE_5Ow2JkZVUsGTCxNY8bAlo1AZ7Lv8yPY")  # o coloca tu token directamente
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.run_polling()

