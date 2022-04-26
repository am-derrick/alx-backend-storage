#!/usr/bin/env python3
"""returns list of school with specific topics"""


def schools_by_topic(mongo_collection, topic):
    """returns list of school by topic"""
    return mongo_collection.find({"topics": topic})
