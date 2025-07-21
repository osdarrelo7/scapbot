from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token de tu bot (NO compartas esto en producción)
TOKEN = "7352077618:AAE_5Ow2JkZVUsGTCxNY8bAlo1AZ7Lv8yPY"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot de soporte SCAP. ¿En qué puedo ayudarte?")

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Puedes usar los comandos disponibles para interactuar conmigo.")

# Inicializa y ejecuta el bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 Bot en ejecución...")
    app.run_polling()


