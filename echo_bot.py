from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8176977256:AAFpkbhz2JctYDl71djHZORexTUnj_Q4Yqc"  # Замените на токен от @BotFather
BOT_USERNAME = "@BotAssistant122121bot"  # Например, @SimpleHelperBot

# Ответ на /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я простой бот. Напиши /help, чтобы узнать, что я умею.")

# Ответ на /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Я понимаю только команды:\n/start - начать общение\n/help - помощь")

# Ответ на ЛЮБОЕ другое сообщение
async def unknown_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Не знаю")

# Запуск бота
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Обработчики команд
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Обработчик ВСЕХ остальных сообщений (включая текст, стикеры, голосовые и т.д.)
    app.add_handler(MessageHandler(filters.ALL, unknown_input))

    print("Бот запущен...")
    app.run_polling()