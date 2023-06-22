#!/usr/bin/env python3
'''Mondodb in Python'''

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    '''returns the list of school having a specific topic'''
    result = mongo_collection.find({'topics': topic})
    return list(result)
