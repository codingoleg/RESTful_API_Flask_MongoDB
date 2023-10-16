import pymongo

import config

db_client = pymongo.MongoClient(f'mongodb://{config.DB_HOST}:{config.DB_PORT}/')
current_db = db_client[config.DB_NAME]
collection = current_db[config.COLLECTION_NAME]

# Создаем отдельный индекс хэша для быстрого поиска по нему
collection.create_index('hash')