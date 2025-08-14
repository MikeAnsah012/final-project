from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password, db_name="AAC", collection_name="animals"):
        try:
            self.client = MongoClient(f"mongodb://{username}:{password}@localhost:27017/{db_name}")
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
            print("Connected to MongoDB successfully.")
        except ConnectionFailure as e:
            print(f"Connection failed: {e}")
            raise

    # CREATE
    def create(self, data):
        if data and isinstance(data, dict):
            result = self.collection.insert_one(data)
            return result.acknowledged
        return False

    # READ with optional query and limit
    def read(self, query={}, limit=0):
        try:
            cursor = self.collection.find(query)
            if limit > 0:
                cursor = cursor.limit(limit)
            return list(cursor)
        except Exception as e:
            print(f"Read failed: {e}")
            return []

    # UPDATE with flexible update logic
    def update(self, query, new_values):
        if not query or not new_values:
            return 0
        try:
            result = self.collection.update_many(query, {'$set': new_values})
            return result.modified_count
        except Exception as e:
            print(f"Update failed: {e}")
            return 0

    # DELETE
    def delete(self, query):
        if not query:
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete failed: {e}")
            return 0

    # ADVANCED: Filter adoptable animals by traits
    def get_adoptable_animals(self, species=None, age_range=None, breed=None, trained=None):
        query = {"status": "adoptable"}

        if species:
            query["animal_type"] = species
        if breed:
            query["breed"] = breed
        if trained is not None:
            query["trained"] = trained
        if age_range and isinstance(age_range, tuple):
            query["age_upon_outcome_in_weeks"] = {"$gte": age_range[0], "$lte": age_range[1]}

        return self.read(query)

    # ADVANCED: Aggregation example — count by breed
    def count_animals_by_breed(self, limit=10):
        try:
            pipeline = [
                {"$group": {"_id": "$breed", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": limit}
            ]
            return list(self.collection.aggregate(pipeline))
        except Exception as e:
            print(f"Aggregation failed: {e}")
            return []

    # ADVANCED: Find by ObjectId
    def find_by_id(self, object_id):
        try:
            return self.collection.find_one({"_id": ObjectId(object_id)})
        except Exception as e:
            print(f"Find by ID failed: {e}")
            return None
