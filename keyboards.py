from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def download_type_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 فيديو", callback_data="type_video")],
        [InlineKeyboardButton("🔇 فيديو بدون صوت", callback_data="type_mute")],
        [InlineKeyboardButton("🎧 صوت فقط", callback_data="type_audio")]
    ])

def quality_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("1080p", callback_data="q_1080"),
            InlineKeyboardButton("720p", callback_data="q_720")
        ],
        [
            InlineKeyboardButton("480p", callback_data="q_480"),
            InlineKeyboardButton("360p", callback_data="q_360")
        ]
    ])