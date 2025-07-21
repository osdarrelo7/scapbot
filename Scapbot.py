from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

TOKEN = "7352077618:AAE_5Ow2JkZVUsGTCxNY8bAlo1AZ7Lv8yPY"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy el bot de soporte de SCAP Firm. ¿En qué puedo ayudarte?")

# Comando /help (opcional)
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponibles:\n/start - Iniciar el bot\n/help - Ver ayuda")

# Crear la aplicación del bot
app = ApplicationBuilder().token(TOKEN).build()

# Agregar los handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

# Ejecutar el bot
if __name__ == "__main__":
    app.run_polling()




