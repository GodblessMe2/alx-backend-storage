#!/usr/bin/env python3
""" 
  Insert aa new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
      Insert doc
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
