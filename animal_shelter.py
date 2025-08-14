# Original animal shelter CRUD script
from pymongo import MongoClient

class AnimalShelter:
    def __init__(self, username, password):
        self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017')
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    def create(self, data):
        return self.collection.insert_one(data).acknowledged

    def read(self, query):
        return list(self.collection.find(query))

    def update(self, query, new_values):
        return self.collection.update_many(query, {'$set': new_values}).modified_count

    def delete(self, query):
        return self.collection.delete_many(query).deleted_count
