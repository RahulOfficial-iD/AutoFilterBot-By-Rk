import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.database import db
from utils.imdb import get_movie_details # External helper

@Client.on_message(filters.group & filters.text & ~filters.command(["start", "help"]))
async def auto_filter(client, message):
    query = message.text
    # 1. Database mein search karo
    files = await db.get_search_results(query)

    if not files:
        # 2. Agar nahi mila toh "Spelling Check" ya "Request" logic
        btn = [[InlineKeyboardButton("Request Movie 🎥", url="https://t.me/your_request_group")]]
        return await message.reply_text(
            f"❌ **'{query}'** nahi mila.\nSahi spelling likhein ya request karein.",
            reply_markup=InlineKeyboardMarkup(btn)
        )

    # 3. Agar mil gaya toh IMDB fetch karo (Optional for speed)
    imdb_data = await get_movie_details(query)
    caption = f"🎬 **Title:** {imdb_data.get('title', query)}\n" \
              f"⭐️ **Rating:** {imdb_data.get('rating', 'N/A')}\n" \
              f"📂 **Total Files:** {len(files)}\n\n" \
              f"⚡️ *Powered by Your Bot*"

    # 4. Buttons Generate Karo (10GB+ files support buttons mein)
    buttons = []
    for file in files[:10]: # Top 10 results
        size = f"({round(file['file_size'] / (1024**3), 2)} GB)" # Bytes to GB
        buttons.append([InlineKeyboardButton(
            f"📥 {file['file_name']} {size}", 
            callback_data=f"file_{file['file_id']}"
        )])

    await message.reply_photo(
        photo=imdb_data.get('poster', 'https://default_poster.jpg'),
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
