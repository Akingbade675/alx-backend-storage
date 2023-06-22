#!/usr/bin/env python3
'''Mondodb in Python'''

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx
    print('{} logs'.format(nginx.count_documents({})))
    print('Methods')
    print('\tmethod GET: {}'.format(nginx.count_documents({'method': 'GET'})))
    print('\tmethod POST: {}'.format(nginx.count_documents(
                                                        {'method': 'POST'}
                                                        )))
    print('\tmethod PUT: {}'.format(nginx.count_documents(
                                                        {'method': 'PUT'}
                                                        )))
    print('\tmethod PATCH: {}'.format(nginx.count_documents(
                                                        {'method': 'PATCH'}
                                                        )))
    print('\tmethod DELETE: {}'.format(nginx.count_documents(
                                                        {'method': 'DELETE'}
                                                        )))
    print('{} status check'.format(nginx.count_documents({'$and': [{'path': '/status'}, {'method': 'GET'}]})))
    client.close()
