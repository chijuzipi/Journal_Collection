from pymongo import MongoClient

class Mongo:
  def __init__(self, journal):
    client = MongoClient()
    self.db = client.UNIFY
    self.collection = self.db[journal]

  def insert(self, content):
    self.collection.insert(content)
    
