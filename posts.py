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

def retrieve(id):
    ''' Retrieve post with given id. '''
    postData = db.posts.find_one({'id': id})
    return None if postData is None else Post(postData)

def create(post):
    return db.posts.insert(dict(post))
