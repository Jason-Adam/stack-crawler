import os
import pymongo

MONGO_DB = os.environ.get("MONGO_DB")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION")
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = os.environ.get("MONGO_PORT")
MONGO_URI = f"mongodb://{MONGO_HOST}"


class MongoPipeline(object):
    def __init__(
        self, mongo_uri=MONGO_URI, mongo_db=MONGO_DB, collection_name=MONGO_COLLECTION
    ):
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db]
        self.collection = pymongo.collection.Collection(
            database=db, name=collection_name
        )

    def process_item(self, item, spider):
        self.collection.update_many(
            {"url": item["url"]}, {"$set": {"question": item["question"]}}, upsert=True
        )
        return item
