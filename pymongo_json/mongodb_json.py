# --------------------------------------------------------------
# Script Name  : import_report_log.py
# Description  : This script connects to a local MongoDB instance
#                using PyMongo, selects the 'cppCheck' database and
#                the 'cppCheck' collection, then imports all documents
#                from 'report_log_simple.json' using bulk_write.
#                The JSON file must contain an array of documents.
#
# Requirements :
#   - MongoDB server running locally on port 27017
#   - PyMongo installed (pip install pymongo)
#   - A valid JSON file: 'report_log_simple.json'
#
# Notes        :
#   - All documents from the JSON array are inserted as-is.
#   - Duplicate '_id' fields will cause MongoDB insertion errors.
#   - The collection 'cppCheck' will be created automatically if
#     it does not already exist.
#
# Author       : Vivien
# Date         : 2026-02-02
# --------------------------------------------------------------

import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("localhost", 27017)
db=client.cppCheck
collection = db.cppCheck
requesting = []

with open(r"report_log_simple.json") as f:
    data = json.load(f)  # Load entire JSON array at once
    for myDict in data:
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()