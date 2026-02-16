from pyrogram import Client, idle
from config import Config

# Plugins folder se sab kuch auto-load karne ke liye
app = Client(
    "Best_Auto_Filter_Bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

async def start_bot():
    await app.start()
    print("🚀 Bot is Online and Indexing Ready!")
    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(start_bot())
