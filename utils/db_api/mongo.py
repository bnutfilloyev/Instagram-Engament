from pymongo import MongoClient
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data.config import IP

client = MongoClient(IP)
storage = MemoryStorage()

database = client['Instagram-Engament']
user_db = database['users']
post_db = database['posts']
