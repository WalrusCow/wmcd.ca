import functools
import hashlib
from datetime import datetime

import db

class Post():
    _FIELDS = ('body', 'title', 'author')
    _HASH_FIELDS = _FIELDS + ('timestamp',)
    _ALL_FIELDS = _HASH_FIELDS + ('id',)

    def __init__(self, kvp):
        for field in Post._FIELDS:
            if field not in kvp:
                self.valid = False
                return
            setattr(self, field, kvp[field])
        self.valid = True
        self.timestamp = kvp.get('timestamp', datetime.now())
        self.id = kvp.get('id', self._hash()[:16])

    def __iter__(self):
        for field in Post._ALL_FIELDS:
            yield field, getattr(self, field)

    def _hash(self):
        ''' Compute a hash of the current object. '''
        hasher = hashlib.sha256()
        for field in Post._HASH_FIELDS:
            hasher.update(str(getattr(self, field)).encode())
        return hasher.hexdigest()

def toPost(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        postData = func(*args, **kwargs)
        return Post(postData) if postData is not None else None
    return wrapper

@toPost
def previousPost(post):
    ''' Return the post immediately before this one. '''
    return db.posts.find_one({'timestamp': {'$lt': post.timestamp}},
                             sort=[('timestamp', -1)])

@toPost
def nextPost(post):
    ''' Return the post immediately after this one, if any. '''
    return db.posts.find_one({'timestamp': {'$gt': post.timestamp}},
                             sort=[('timestamp', 1)])

@toPost
def retrieve(id):
    ''' Retrieve post with given id. '''
    return db.posts.find_one({'id': id})

def create(post):
    return db.posts.insert(dict(post))
