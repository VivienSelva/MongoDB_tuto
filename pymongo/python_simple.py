# my first scripte using pymongo, I already created DB and collection using the mongo shell,now i will use python to connect to the DB a
# --------------------------------------------------------------
# Script Name  : pymongo_test.py
# Description  : This script connects to a MongoDB instance using
#                PyMongo, selects the 'cppCheck' database, and
#                displays one document from the 'cppCheck' collection.
#                The database and collection must already exist
#                (created previously in the mongo shell).
#
# Requirements :
#   - MongoDB server running locally on port 27017
#   - PyMongo installed (pip install pymongo)
#
# Author       : Vivien
# Date         : 2026-01-30
# ----

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db=client.cppCheck
print(db.cppCheck.find_one())