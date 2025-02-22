from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# ⚠️ توکن رباتت رو اینجا قرار بده
TOKEN = "8114459206:AAFq15XkiIsGUfyXGoSqHu-Asw0MlNNtZ4Q"

# تابعی که وقتی کاربر "/start" رو بفرسته اجرا می‌شه
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! من ربات تلگرامی تو هستم. چطور می‌تونم کمکت کنم؟")

# تابعی که وقتی کاربر "/help" رو بفرسته اجرا می‌شه
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("دستورات موجود:\n/start - شروع\n/help - راهنما")

# راه‌اندازی ربات
def main():
    app = Application.builder().token(TOKEN).build()

    # اضافه کردن دستورات به ربات
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # اجرای ربات
    print("✅ ربات فعال شد!")
    app.run_polling()

if __name__ == "__main__":
    main()
