import uuid
from flask import make_response
import mongo


class User:
    def add_user(self, username, password):
        if not mongo.collection.find_one({"username": username}):
            params = {
                'username': username,
                'password': password
            }
            mongo.collection.save(params)
            return 'A new account has been created. ' + \
                   'Login: ' + username + ', ' + \
                   'Password: ' + password
        else:
            return 'Login is used.'

    def login_user(self, username, password):
        if mongo.collection.find_one({"username": username, "password": password}):
            uuid_user = uuid.uuid4().hex
            resp = make_response('Login successful')
            resp.set_cookie('session', uuid_user)
            User().update_user_cookie(username=username, cookie=uuid_user)
            return resp
        else:
            return 'Invalid username/password'

    def update_user(self, session, username='', password=''):
        if mongo.collection.find_one({"session": session}):
            if username == '':
                mongo.collection.update({'session': session}, {'$set': {"password": password}})
                return 'New password: ' + password
            elif password == '':
                if not mongo.collection.find_one({"username": username}):
                    mongo.collection.update({'session': session}, {'$set': {"username": username}})
                    return 'New login: ' + username
                else:
                    return 'Login is used.'
            else:
                if not mongo.collection.find_one({"username": username}):
                    mongo.collection.update({'session': session},
                                            {'$set': {"username": username, "password": password}})
                    return 'New login: ' + username + ', ' + \
                           'New password: ' + password
        else:
            return 'You are not loged in.'

    def exist_user(self, username, password):
        if mongo.collection.find_one({"username": username, "password": password}):
            return True
        else:
            return False

    def remove_user(self, username, password):
        #delete_all_user_files()
        mongo.collection.remove({"username": username, "password": password})
        return 'The user was deleted.'

    def remove_user2(self, session):
        if mongo.collection.find_one({"session": session}):
            # delete_all_user_files()
            mongo.collection.remove({"session": session})
            return 'The user was deleted.'
        else:
            return 'You are not loged in.'

    def find_username(self, cookie):
        if mongo.collection.find_one({'session': cookie}):
            n = mongo.collection.find_one({'session': cookie})
            return n['_id']
        else:
            return 'You are not authorized'

    def update_user_cookie(self, username, cookie):
        mongo.collection.update({'username': username}, {"$set": {"session": cookie}})
