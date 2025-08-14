# Refactored animal shelter module with validation and logging
from pymongo import MongoClient, errors
from utils.validator import validate_animal_data
import logging

logging.basicConfig(level=logging.INFO)

class AnimalShelter:
    def __init__(self, username, password):
        try:
            self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017')
            self.database = self.client['AAC']
            self.collection = self.database['animals']
        except errors.ConnectionFailure as e:
            logging.error(f"Connection failed: {e}")
            raise

    def create(self, data):
        if validate_animal_data(data):
            return self.collection.insert_one(data).acknowledged
        return False

    def read(self, query):
        return list(self.collection.find(query))

    def update(self, query, new_values):
        return self.collection.update_many(query, {'$set': new_values}).modified_count

    def delete(self, query):
        return self.collection.delete_many(query).deleted_count
