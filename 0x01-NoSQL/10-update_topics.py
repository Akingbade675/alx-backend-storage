#!/usr/bin/env python3
'''Mondodb in Python'''

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    '''changes all topics of a school document based on the name'''
    result = mongo_collection.update_one(
                                        {'name': name},
                                        {'$set': {'topics': topics}})
    return result
