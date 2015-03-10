import base64
import os
from datetime import datetime, timedelta

import blog.db as db

SESSION_ID_SIZE = 128

class Session:
    def __init__(self, user):
        ''' Create a new session for the given user. '''
        self.id = base64.b16encode(os.urandom(SESSION_ID_SIZE)).decode()
        self.expiresAt = datetime.utcnow() + timedelta(hours=6)
        self.user = user

        db.sessions.insert({'id': self.id,
                            'user': user,
                            'expireAt': self.expiresAt})

    @staticmethod
    def exists(user, id):
        ''' Check if the given (user, id) is a valid session. '''
        return db.sessions.find_one({'id': id, 'user': user}) is not None
