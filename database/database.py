import motor.motor_asyncio
from config import MONGO_DB_URI, DATABASE_NAME

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.files  # Files store karne ke liye collection

    # 1. New File Save Karna (Indexing)
    async def add_file(self, file_data):
        # Check if file already exists using file_id
        if not await self.col.find_one({'file_id': file_data['file_id']}):
            await self.col.insert_one(file_data)
            return True
        return False

    # 2. File Search Logic (Regex Search)
    async def get_search_results(self, query):
        # 'i' means case-insensitive search
        filter = {'file_name': {'$regex': query, '$options': 'i'}}
        cursor = self.col.find(filter)
        results = await cursor.to_list(length=100) # Max 100 results
        return results

    # 3. Stats Check (Kitni files index ho chuki hain)
    async def get_total_files(self):
        return await self.col.count_documents({})

# Database instance create karna
db = Database(MONGO_DB_URI, DATABASE_NAME)
