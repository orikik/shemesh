from user.DB_user_func import User


class Correct:
    def add(self, data):
        key1 = 'username' in data
        key2 = 'password' in data
        if key1 and key2 and len(data) == 2:
            n = User().add_user(username=data['username'], password=data['password'])
            return n
        else:
            return 'Incorrect data.', 400

    def login(self, data):
        key1 = 'username' in data
        key2 = 'password' in data
        if key1 and key2 and len(data) == 2:
            n = User().login_user(username=data['username'], password=data['password'])
            return n
        else:
            return 'Incorrect data.', 400

    def update(self, data, session):
        key1 = 'username' in data
        key2 = 'password' in data
        if key1 and key2 and len(data) == 2:
            n = User().update_user(username=data['username'], password=data['password'], session=session)
            return n
        if key1 and len(data) == 1:
            n = User().update_user(username=data['username'], session=session)
            return n
        if key2 and len(data) == 1:
            n = User().update_user(password=data['password'], session=session)
            return n
        else:
            return 'Incorrect data.', 400

    def remove(self, data):
        key1 = 'username' in data
        key2 = 'password' in data
        if key1 and key2 and len(data) == 2:
            if User().exist_user(username=data['username'], password=data['password']):
                n = User().remove_user(username=data['username'], password=data['password'])
                return n
            else:
                return 'Wrong password or user with such login does not exist.'
        else:
            return 'Incorrect data.', 400