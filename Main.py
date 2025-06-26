import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

allowed_users = [
    "BanditAnt", "Алексейкрасавчик", "ГорыныЧ", "romzes", "ДАНУНАХ",
    "rulant", "тихон", "simay", "Hizir", "Mlg174", "Юрий", "Kasia",
    "Антон Ялта", "Sekhmet"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    if user_name in allowed_users:
        await update.message.reply_text("Добро пожаловать! Вот ваша ссылка: https://t.me/+dkNKOiy7TlAwMTVi")
    else:
        await update.message.reply_text("Извините, вы не в списке приглашённых.")

def main():
    token = os.getenv("BOT_TOKEN")
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
