import os
from keyboards import download_type_keyboard, quality_keyboard
from downloader import download_video, download_audio, download_video_no_audio
from subscription import check_subscription, force_subscribe
from users import save_user

async def start(update, context):
    if not await check_subscription(context.bot, update.effective_user.id):
        return await force_subscribe(update)

    save_user(update.effective_user)
    await update.message.reply_text(
        "👋 أرسل رابط الفيديو وسيتم تحميله لك مباشرة 🎬"
    )

async def handle_link(update, context):
    context.user_data.clear()
    context.user_data["url"] = update.message.text
    await update.message.reply_text(
        "اختر نوع التحميل 👇",
        reply_markup=download_type_keyboard()
    )

async def button_handler(update, context):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("type_"):
        context.user_data["type"] = data
        if data == "type_audio":
            file_path = download_audio(context.user_data["url"])
            await query.message.reply_audio(audio=open(file_path, "rb"))
            os.remove(file_path)
        else:
            await query.message.reply_text(
                "اختر الجودة 👇",
                reply_markup=quality_keyboard()
            )

    elif data.startswith("q_"):
        quality = data.split("_")[1]
        url = context.user_data["url"]
        t = context.user_data["type"]

        if t == "type_video":
            file_path = download_video(url, quality)
            await query.message.reply_video(video=open(file_path, "rb"))

        elif t == "type_mute":
            file_path = download_video_no_audio(url, quality)
            await query.message.reply_video(video=open(file_path, "rb"))

        os.remove(file_path)