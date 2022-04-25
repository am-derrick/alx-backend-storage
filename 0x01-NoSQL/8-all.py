#!/usr/bin/env python3
"""lists all documents in collection"""


def list_all(mongo_collection):
    """returns list of ll documents or empty list"""
    return [each for each in mongo_collection.find()]
