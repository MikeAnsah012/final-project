from pymongo import MongoClient

class AnimalShelter:
    def __init__(self, username, password):
        self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017/')
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    def read_all(self):
        return list(self.collection.find())

    def find_by_type(self, animal_type):
        return list(self.collection.find({"animal_type": animal_type}))
