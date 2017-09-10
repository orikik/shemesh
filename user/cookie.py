import uuid
from flask import make_response


class Cookie:
    def get_cookie(self, username):
        uuid_user = uuid.uuid4().hex
        resp = make_response('Login successful')
        resp.set_cookie('session', uuid_user)
        User().update_user_cookie(username=username, cookie=uuid_user)
        return resp
