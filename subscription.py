from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHANNEL_USERNAME, CHANNEL_URL

async def check_subscription(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

async def force_subscribe(update):
    keyboard = [
        [InlineKeyboardButton("📢 اشترك بالقناة", url=CHANNEL_URL)]
    ]
    await update.message.reply_text(
        "❌ لا يمكنك استخدام البوت بدون الاشتراك بالقناة",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )