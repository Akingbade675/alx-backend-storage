#!/usr/bin/env python3
'''MongoDB in Python'''


from pymongo import MongoClient


def list_all(mongo_collection):
    '''lists all documents in a collection'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    result = school_collection.find()
    print(result)
    return result



if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
