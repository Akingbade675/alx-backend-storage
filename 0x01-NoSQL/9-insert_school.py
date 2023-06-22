#!/usr/bin/env python3
'''Mongodb in Python'''

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document in a collection based on kwargs'''
    result = mongo_collection.insert_one(kwargs)
    return result
