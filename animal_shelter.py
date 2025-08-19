import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from typing import Optional, Dict, Any, List


class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self):
        """Initialize the MongoDB connection using environment variables."""
        try:
            username = os.getenv('MONGO_USER', 'aacuser')
            password = os.getenv('MONGO_PASS', 'SNHU1234')
            host = os.getenv('MONGO_HOST', 'nv-desktop-services.apporto.com')
            port = int(os.getenv('MONGO_PORT', 31517))
            db = os.getenv('MONGO_DB', 'AAC')
            collection = os.getenv('MONGO_COLLECTION', 'animals')

            uri = f'mongodb://{username}:{password}@{host}:{port}'
            self.client = MongoClient(uri)
            self.database = self.client[db]
            self.collection = self.database[collection]
            self.client.admin.command('ping')  # Confirm connection
            print("MongoDB connection established.")
        except Exception as e:
            print("Failed to connect to MongoDB:", e)
            raise

    def create(self, data: Optional[Dict[str, Any]]) -> bool:
        """Insert a document into the collection."""
        if not data or not isinstance(data, dict):
            print("Invalid data format for insertion.")
            return False
        try:
            result = self.collection.insert_one(data)
            print("Inserted document ID:", result.inserted_id)
            return result.acknowledged
        except PyMongoError as e:
            print("Insert failed:", e)
            return False

    def read(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Query documents from the collection."""
        try:
            search_filter = criteria if isinstance(criteria, dict) else {}
            result = list(self.collection.find(search_filter))
            print(f"Read {len(result)} document(s).")
            return result
        except PyMongoError as e:
            print("Read failed:", e)
            return []

    def update(self, query: Optional[Dict[str, Any]], update_ops: Optional[Dict[str, Any]]) -> bool:
        """Update documents matching the query with update operators like $set."""
        if not query or not isinstance(query, dict):
            print("Invalid query for update.")
            return False
        if not update_ops or not isinstance(update_ops, dict):
            print("Invalid update data.")
            return False
        try:
            result = self.collection.update_many(query, update_ops)
            print(f"Modified {result.modified_count} document(s).")
            return result.modified_count > 0
        except PyMongoError as e:
            print("Update failed:", e)
            return False

    def delete(self, query: Optional[Dict[str, Any]]) -> bool:
        """Delete documents matching the query."""
        if not query or not isinstance(query, dict):
            print("Invalid query for deletion.")
            return False
        try:
            result = self.collection.delete_many(query)
            print(f"Deleted {result.deleted_count} document(s).")
            return result.deleted_count > 0
        except PyMongoError as e:
            print("Delete failed:", e)
            return False
