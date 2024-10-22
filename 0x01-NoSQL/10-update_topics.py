#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """ Update the topics of a school """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
