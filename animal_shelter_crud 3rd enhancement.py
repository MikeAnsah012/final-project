from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host='localhost', port=27017, db_name='AAC', collection='animals'):
        try:
            self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/')
            self.database = self.client[db_name]
            self.collection = self.database[collection]
            print("Connected to MongoDB successfully.")
        except errors.ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")
            raise

    def create_animal(self, animal_data):
        """Insert a new animal document into the collection"""
        if animal_data and isinstance(animal_data, dict):
            try:
                result = self.collection.insert_one(animal_data)
                print(f"Animal inserted with ID: {result.inserted_id}")
                return True
            except Exception as e:
                print(f"Create Error: {e}")
                return False
        else:
            print("Invalid animal data provided.")
            return False

    def read_animals(self, query={}, limit=10):
        """Read and return animal documents matching the query"""
        try:
            return list(self.collection.find(query).limit(limit))
        except Exception as e:
            print(f"Read Error: {e}")
            return []

    def update_animal(self, animal_id, update_data):
        """Update an animal document by its ObjectId"""
        if not ObjectId.is_valid(animal_id):
            print("Invalid ObjectId.")
            return False
        if not update_data:
            print("No update data provided.")
            return False
        try:
            result = self.collection.update_one({'_id': ObjectId(animal_id)}, {'$set': update_data})
            if result.matched_count > 0:
                print(f"Updated {result.modified_count} document(s).")
                return True
            else:
                print("No document found with that ID.")
                return False
        except Exception as e:
            print(f"Update Error: {e}")
            return False

    def delete_animal(self, animal_id):
        """Delete an animal document by its ObjectId"""
        if not ObjectId.is_valid(animal_id):
            print("Invalid ObjectId.")
            return False
        try:
            result = self.collection.delete_one({'_id': ObjectId(animal_id)})
            if result.deleted_count > 0:
                print(f"Deleted {result.deleted_count} document(s).")
                return True
            else:
                print("No document found with that ID.")
                return False
        except Exception as e:
            print(f"Delete Error: {e}")
            return False
