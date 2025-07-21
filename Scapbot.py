from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

print("Bot inicializando...")

TOKEN = "7352077618:AAE_5Ow2JkZVUsGTCxNY8bAlo1AZ7Lv8yPY"  # ← Reemplaza esto con tu token real
print(f"Token cargado: {TOKEN[:10]}********")

# Handler para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Comando /start recibido de {update.effective_user.username}")
    await update.message.reply_text("Hola Oscar, bienvenido al Soporte de SCAP Firm.\n¿En qué podemos ayudarte hoy?")

# Handler para cualquier texto (que no sea comando)
async def responder_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f"Mensaje recibido: {update.message.text} de {update.effective_user.username}")
    await update.message.reply_text("Hola! Por favor adjunta un documento o imagen para validar tu dirección.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Agrega los handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_mensaje))

    print("✅ Bot corriendo y esperando mensajes...")
    app.run_polling()
