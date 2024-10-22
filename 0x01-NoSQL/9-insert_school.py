#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """ Insert a school into the collection """
    return mongo_collection.insert_one(kwargs).inserted_id
