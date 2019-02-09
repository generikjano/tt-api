import os

DB_NAME = 'postgres'
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5438')
DB_USER = 'postgres'
DB_PASSWORD = 'passw0rd@1'
DB_CONNECTION_STRING = 'postgresql://{user}:{password}@{host}/{db}'.format(user=DB_USER, password=DB_PASSWORD,
                                                                           host='{}:{}'.format(DB_HOST, DB_PORT), db=DB_NAME)
SCHEMA = 'clients'
