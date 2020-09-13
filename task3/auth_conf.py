"""модуль аутентификации пользовая и выдачи токена"""
from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    """ищет пользователя в БД по имени и сравнивает введенный пароль и пароль из БД"""
    user = User.search_username(username) #user_names.get(username, None)
    if (user is not None) and safe_str_cmp(user.password, password):
        return user
    return None

def identity(data):
    """ищет пользователя в БД по id, гененирует и возвращает токен"""
    uid = data['identity']
    return User.search_id(uid) #user_ids.get(uid, None)

if __name__ == "__main__":
    pass
