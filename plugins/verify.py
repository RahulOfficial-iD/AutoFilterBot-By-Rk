import time
from database.database import db

# Shortener API Details
SHORTENER_API = "your_api_key"
SHORTENER_URL = "gplinks.in" # Example

async def is_user_verified(user_id):
    user = await db.col.users.find_one({'user_id': user_id})
    if not user or 'last_verified' not in user:
        return False
    
    # Check if 24 hours (86400 seconds) have passed
    last_verified = user['last_verified']
    if (time.time() - last_verified) < 86400:
        return True
    return False

async def update_verification(user_id):
    await db.col.users.update_one(
        {'user_id': user_id},
        {'$set': {'last_verified': time.time()}},
        upsert=True
    )
