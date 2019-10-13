import pymongo


class MongoPipeline(object):
    def __init__(
        self,
        mongo_uri="mongodb://localhost",
        mongo_db="stackoverflow",
        collection_name="ai_questions",
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
