#!/usr/bin/env python3
'''MongoDB in Python'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''lists all documents in a collection'''
    result = mongo_collection.find()
    return result
