#!/usr/bin/env python3
""" 
  Provides some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient


def log_stats():
    """ 
       log stats
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collections = client.logs.nginx
    total = logs_collections.count_documents({})
    get = logs_collections.count_documents({"method": "GET"})
    post = logs_collections.count_documents({"method": "POST"})
    put = logs_collections.count_documents({"method": "PUT"})
    patch = logs_collections.count_documents({"method": "PATCH"})
    delete = logs_collections.count_documents({"method": "DELETE"})
    path = logs_collections.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")

if __name__ == "__main__":
    log_stats()
