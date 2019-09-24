import pymongo


class MongoPipeline(object):

    collection_name = "ai_questions"

    def __init__(self, mongo_uri="mongodb://localhost", mongo_db="stackoverflow"):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.update({'url': item['url']}, dict(item), upsert=True)
        return item
