#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """ List all documents in a collection """
    return list(mongo_collection.find())
