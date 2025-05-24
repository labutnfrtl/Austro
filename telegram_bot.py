from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import time

# Reemplaza 'TU_TOKEN' con el token que obtuviste de BotFather
TOKEN =  'TU_TOKEN'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Soy tu bot. Envíame 'clima' para leer las primeras 4 líneas de infos.txt, 'error' para leer el archivo error.txt, 'datos' para recibir el archivo backup.csv, o 'comandos' para ver la lista de comandos.")

async def send_commands_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands_list = (
        "Aquí tienes la lista de comandos disponibles:\n\n"
        "1. 'clima': Muestra el ultimo registro de los sensores.\n"
        "2. 'error': Muestra los errores ocurridos.\n"
        "3. 'datos': Recibe el archivo backup.csv el cual contiene el registro de los sensores.\n"
        "4. 'comandos': Muestra esta lista de comandos.\n"
    )
    await update.message.reply_text(commands_list)

async def read_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text.lower()
    
    if "clima" in message_text:
        try:
            with open('infos.txt', 'r') as file:
                lines = file.readlines()
                content = "".join(lines)
                if len(lines) >= 4:
                    content = "".join(lines[:4])
                else:
                    content = "No se pudo leer los datos del clima.\n\nEstado actual programa:\n" + content
                await update.message.reply_text(content)
        except FileNotFoundError:
            await update.message.reply_text("El archivo infos.txt no se encuentra.")
    
    elif "error" in message_text:
        try:
            with open('error.txt', 'r') as file:
                content = file.read()
                await update.message.reply_text(content)
        except FileNotFoundError:
            await update.message.reply_text("El archivo error.txt no se encuentra.")
    
    elif "datos" in message_text:
        await send_backup_file(update, context)
    
    elif "comandos" in message_text:
        await send_commands_list(update, context)
    
    else:
        await update.message.reply_text("Comando no reconocido. Envíame 'comandos' para ver la lista de comandos.")

async def send_backup_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_path = 'backup.csv'
    
    # Esperar hasta que el archivo esté disponible
    while True:
        try:
            with open(file_path, 'rb') as file:
                await update.message.reply_document(document=InputFile(file, filename='backup.csv'))
                break
        except IOError:
            await update.message.reply_text("El archivo backup.csv está en uso, intentando de nuevo...")
            time.sleep(5)  # Espera de 5 segundos antes de intentar nuevamente

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, read_file))

    application.run_polling()

if __name__ == '__main__':
    main()
