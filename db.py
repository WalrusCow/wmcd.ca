import pymongo

DB_URL = 'localhost'
DB_PORT = 27017

BLOG_DB = 'blog'
POSTS_COLLECTION = 'posts'
ACCOUNTS_COLLECTION = 'accounts'
SESSIONS_COLLECTION = 'sessions'

_client = pymongo.MongoClient(DB_URL, DB_PORT)
_db = _client[BLOG_DB]
posts = _db[POSTS_COLLECTION]
accounts = _db[ACCOUNTS_COLLECTION]
sessions = _db[SESSIONS_COLLECTION]

def close():
    _client.close()
