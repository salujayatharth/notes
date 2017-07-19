#!/bin/python3
from pymongo import MongoClient

def connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client["master"]
db = connection()
