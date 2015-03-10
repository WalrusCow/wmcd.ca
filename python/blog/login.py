import functools
import hashlib
from bottle import redirect, request

import blog.db as db
from blog.session import Session

def requiresLogin(func):
    ''' Wrap a request to reject if the user is not logged in. '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sessionId = request.get_cookie('id')
        user = request.get_cookie('user')
        if Session.exists(user, sessionId):
            return func(*args, **kwargs)
        redirect('login')
    return wrapper

def loginUser(user, password):
    ''' Attempt to log the user in with the given password.
    Return a Session if success or an error string on failure. '''
    account = db.accounts.find_one({'user_id': user})
    if account is None:
        return 'No such account'

    hasher = hashlib.sha256()
    hasher.update(account['salt'].encode())
    hasher.update(password.encode())
    passwordHash = hasher.hexdigest()
    if passwordHash != account['password_hash']:
        return 'Incorrect password'

    # Add session
    return Session(user)
