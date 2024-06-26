#!/usr/bin/env python3
"""
This Module handles authtentication functions
"""
from typing import Union
from uuid import uuid4
import jwt
import bcrypt
from flask_jwt_extended import create_access_token
from sqlalchemy.orm.exc import NoResultFound
from flask import request, jsonify
from functools import wraps
from os import getenv

from models import storage
from models.vendor import Vendor

BLACK_LIST_TOKEN = set()
EXEMPT_ENDPOINTS = [
    "api/v1/customers/register",
    "/register",
]

SECRET_KEY = getenv("SECRET_KEY")


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def register_user(self, cls: Union[Vendor], **kwargs):
        """Regitsers a User"""
        email = kwargs.get("email")
        password = kwargs.get("password")
        try:
            user = storage.find_user_by(cls, email=email)
            if user:
                raise ValueError(f"User {user.email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            kwargs["hashed_password"] = hashed_password.decode("utf-8")
            new_user = cls(**kwargs)
            new_user.save()
            return new_user

    def valid_login(self, cls: Union[Vendor], email: str, password: str) -> bool:
        """validated a user"""
        try:
            user = storage.find_user_by(cls, email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"), user.hashed_password.encode("utf-8")
            )
        except NoResultFound:
            return False

    def create_session_token(self, cls: Union[Vendor], email: str) -> Union[str, None]:
        """creates a session token"""
        try:
            user = storage.find_user_by(cls, email=email)
        except NoResultFound:
            return None

        access_token = create_access_token(identity=user.email)
        return access_token

    def destroy_session(self, access_token: str) -> None:
        """destroys the session"""
        BLACK_LIST_TOKEN.add(access_token)

    def creates_reset_password_token(self, cls: Union[Vendor], email: str) -> str:
        """Generates reset password token"""
        try:
            user = storage.find_user_by(cls, email=email)
        except Exception:
            raise ValueError

        reset_token = _generate_uuid()
        try:
            storage.update_user(cls, user.id, reset_token=reset_token)
        except Exception:
            return None

        return reset_token

    def update_password(
        self, cls: Union[Vendor], reset_token: str, password: str
    ) -> None:
        """Updates user password"""
        try:
            user = storage.find_user_by(cls, reset_token=reset_token)
            print(user)
        except Exception:
            raise ValueError

        hashed_password = _hash_password(password)
        storage.update_user(
            cls, user.id, hashed_password=hashed_password, reset_token=None
        )

    @staticmethod
    def token_required(func):
        print(" Testing")

        @wraps(func)
        def decorated(*args, **kwargs):
            token = None

            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]

            if not token:
                return jsonify({"message": "Token is missing!"}), 401

            if request.endpoint in EXEMPT_ENDPOINTS:
                return func(*args, **kwargs)
            else:
                try:
                    data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                    # You can access the user data from the decoded token
                    # current_user = data['user']
                except jwt.ExpiredSignatureError:
                    return jsonify({"message": "Token has expired!"}), 401
                except jwt.InvalidTokenError:
                    return jsonify({"message": "Invalid token!"}), 401

                return func(*args, **kwargs)

        return decorated
