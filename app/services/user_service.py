from typing import Optional

from app.data.user import User


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, 'abc')


def login_user(email: str, password: str) -> Optional[User]:
    if password == 'abc':
        return User("test user", email, 'abc')

    return None
