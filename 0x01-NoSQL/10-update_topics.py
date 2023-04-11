#!/usr/bin/env python3
""" 
  Changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    query = {'name': name}
    val = {'$set': {'topics': topics}}
    mongo_collection.update_many(query, val)
