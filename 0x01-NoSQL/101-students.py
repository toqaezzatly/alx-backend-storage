#!/usr/bin/env python3
""" 101-students """
from pymongo import MongoClient


def top_students(mongo_collection):
    """ Return all students sorted by average score """
    students = mongo_collection.find()
    result = []

    for student in students:
        scores = [topic['score'] for topic in student.get('topics', [])]
        average_score = sum(scores) / len(scores) if scores else 0
        student['averageScore'] = average_score
        result.append(student)

    return sorted(result, key=lambda x: x['averageScore'], reverse=True)
