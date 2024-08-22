# from pymongo import MongoClient
# from datetime import datetime
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = MongoClient(os.getenv("MONGO_URI"))
# db = client.manufacturing
# defects_collection = db.defects

# def insert_defect(defect_type, date, description=None, severity=None):
#     defect = {
#         "defectType": defect_type,
#         "date": datetime.strptime(date, "%Y-%m-%d"),
#         "description": description,
#         "severity": severity
#     }
#     defects_collection.insert_one(defect)

# def find_defects(filters):
#     return list(defects_collection.find(filters))
