#!/usr/bin/env python3
"""
  List all documents in the collection
"""

import pymongo


def list_all(mongo_collection):
    """
      List all
    """
    result = mongo_collection.find()
    return [elm for elm in result]
