#!/usr/bin/env python3
""" 
  Adding the top 10 of the most present IPs in the collection nginx of the database logs
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
    print("IPs:")
    sorted_ips = logs_collections.aggregate(
        [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
         {"$sort": {"count": -1}}])
    i = 0
    for s in sorted_ips:
        if i == 10:
            break
        print(f"\t{s.get('_id')}: {s.get('count')}")
        i += 1


if __name__ == "__main__":
    log_stats()
