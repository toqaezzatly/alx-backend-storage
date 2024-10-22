#!/usr/bin/env python3
""" 101-students """

def top_students(mongo_collection):
    """ Return the top students """
    return mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
