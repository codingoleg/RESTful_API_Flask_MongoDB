import os

# Flask options
FLASK_HOST: str = os.environ['FLASK_HOST']
FLASK_PORT: int = int(os.environ['FLASK_PORT'])

# MongoDB options
# DB_HOST should be the same as the name of the service in docker-compose.yml
# or DB_HOST = 'localhost' for local usage.
DB_HOST: str = os.environ['DB_HOST']
DB_PORT: str = os.environ['DB_PORT']
DB_NAME: str = os.environ['DB_NAME']
COLLECTION_NAME: str = os.environ['COLLECTION_NAME']
