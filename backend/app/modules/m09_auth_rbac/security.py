"""Password hashing (bcrypt via passlib) and JWT access + refresh token creation/verification.

Belongs to: Module 9 Login & Role-Based Access.
"""

def hash_password(password: str) -> str:
    pass


def verify_password(plain_password: str, hashed_password: str) -> bool:
    pass


def create_access_token(subject: str) -> str:
    pass


def create_refresh_token(subject: str) -> str:
    pass


def decode_token(token: str) -> dict:
    pass
