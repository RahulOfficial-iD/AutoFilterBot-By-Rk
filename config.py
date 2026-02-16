import os

class Config:
    API_ID = int(os.environ.get("API_ID", "12345"))
    API_HASH = os.environ.get("API_HASH", "your_hash")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_token")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "your_mongodb_url")
    ADMINS = [12345678, 98765432] # Aapki user ID
