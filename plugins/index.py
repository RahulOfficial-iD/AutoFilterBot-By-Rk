import asyncio
from pyrogram import Client, filters
from database.database import db # Jo humne pehle banaya
from pyrogram.errors import FloodWait

@Client.on_message(filters.command("index") & filters.user(ADMINS))
async def index_files(client, message):
    if len(message.command) < 2:
        return await message.reply("Channel ID do! Example: `/index -100123456789`")

    chat_id = message.command[1]
    status = await message.reply("Indexing Shuru ho rahi hai... 🔄")
    
    count = 0
    async for msg in client.get_chat_history(chat_id):
        file = msg.document or msg.video or msg.audio
        if file:
            file_data = {
                "file_name": file.file_name,
                "file_id": file.file_id,
                "file_size": file.file_size, # Handles 10GB+ easily
                "chat_id": chat_id,
                "msg_id": msg.id
            }
            await db.add_file(file_data)
            count += 1
            if count % 100 == 0:
                await status.edit(f"Indexed {count} files...")

    await status.edit(f"✅ Success! {count} files index ho gayi hain.")
