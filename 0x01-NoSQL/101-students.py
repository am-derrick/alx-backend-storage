#!/usr/bin/env python3
"""returns top students"""


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    return list(mongo_collection.find())
