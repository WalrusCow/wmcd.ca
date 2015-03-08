import base64
import os
import hashlib
from getpass import getpass

import db

SALT_SIZE = 128

def main():
    ''' Read a username and password from input and sign up that user. '''
    user = None
    while not user:
        user = input('Username: ').lower()
    while True:
        firstPass = getpass('Enter password: ')
        secondPass = getpass('Repeat password: ')
        if firstPass == secondPass: break
        print('Passwords did not match!')

    salt = base64.b64encode(os.urandom(SALT_SIZE)).decode()
    hasher = hashlib.sha256()
    hasher.update(salt.encode())
    hasher.update(firstPass.encode())
    hash = hasher.hexdigest()
    db.accounts.insert({'user_id': user, 'salt': salt, 'password_hash': hash})

if __name__ == '__main__':
    main()
