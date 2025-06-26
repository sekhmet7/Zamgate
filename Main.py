import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Разрешённые имена
ALLOWED_NAMES = {
    "BanditAnt",
    "Алексейкрасавчик",
    "ГорыныЧ",
    "romzes",
    "ДАНУНАХ",
    "rulant",
    "тихон",
    "simay",
    "Hizir",
    "Mlg174",
    "Юрий",
    "Kasia",
    "Антон Ялта",
    "Sekhmet"
}

# Ссылка на группу
GROUP_LINK = "https://t.me/+dkNKOiy7TlAwMTVi"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Здравствуйте!\nВведите имя как в игре, без ошибок, в точности."
    )

async def check_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    if user_input in ALLOWED_NAMES:
        await update.message.reply_text(
            f"Имя подтверждено. Вот ссылка на группу:\n{GROUP_LINK}"
        )
    else:
        await update.message.reply_text(
            "К сожалению, это имя не найдено в списке."
        )

def main():
    token = os.getenv("BOT_TOKEN")
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_name))

    application.run_polling()

if __name__ == '__main__':
    main()
