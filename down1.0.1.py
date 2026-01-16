from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
from config import BOT_TOKEN
import commands

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", commands.start))

# استقبال أي رسالة نصية (الرابط)
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, commands.handle_link))

# أزرار التحميل
app.add_handler(CallbackQueryHandler(commands.button_handler))

print("🤖 Bot is running...")
app.run_polling()