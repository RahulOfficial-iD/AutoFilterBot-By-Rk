from pyrogram.errors import UserNotParticipant

async def check_fsub(client, message):
    FSUB_CHANNEL = -1001234567890 # Aapka Channel ID
    try:
        await client.get_chat_member(FSUB_CHANNEL, message.from_user.id)
        return True
    except UserNotParticipant:
        await message.reply_text(
            "🛑 **Access Denied!**\n\nFile paane ke liye pehle hamare channel ko join karein.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Join Channel 📢", url="https://t.me/yourchannel")
            ]])
        )
        return False
