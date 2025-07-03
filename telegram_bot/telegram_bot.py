from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import time
from dotenv import load_dotenv
import os

#borrar esto despues.

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

print("Bot iniciado")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Bot saludo")
    await update.message.reply_text("¡Hola! Soy tu bot. Envíame 'clima' para leer las primeras 4 líneas de infos.txt, 'error' para leer el archivo error.txt, 'datos' para recibir el archivo backup.csv, o 'comandos' para ver la lista de comandos.")

async def send_commands_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands_list = (
        "Descargar base de datos comando: datos\n\n"
    )
    await update.message.reply_text(commands_list)

async def read_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text.lower()
    print(message_text)
    if "datos" in message_text:
        await send_db_file(update, context)
    
    elif "comandos" in message_text:
        await send_commands_list(update, context)
    
    else:
        await update.message.reply_text("Comando no reconocido. Envíame 'comandos' para ver la lista de comandos.")

async def send_db_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_path = os.path.join("..", "registros.db")
    
    # Esperar hasta que el archivo esté disponible
    while True:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(document=InputFile(file, filename='registros.db'))
                break
        except IOError:
            await update.message.reply_text("El archivo base de datos  está en uso, intentando de nuevo...")
            time.sleep(5)  # Espera de 5 segundos antes de intentar nuevamente

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, read_file))

    application.run_polling()

if __name__ == '__main__':
    main()