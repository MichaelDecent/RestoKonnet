#!/usr/bin/env python3
"""
This Module handles authtentication functions
"""
from typing import Union, Any
from os import getenv
from .auth import Auth
from dotenv import load_dotenv
from random import randrange
from flask_jwt_extended import create_access_token
from sqlalchemy.orm.exc import NoResultFound

from models import storage
from models.customer import Customer
from vonage import Client, Sms


BLACK_LIST_TOKEN = set()

load_dotenv()
key = getenv("KEY")
secret = getenv("SECRET")


def _create_otp() -> str:
    """Creates OTP"""
    otp = randrange(100000, 999999)
    return otp


def _send_otp(phone_no: str, otp: str) -> bool:
    """Sends OTP to a client"""

    client = Client(key=key, secret=secret)
    sms = Sms(client)

    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": phone_no,
            "text": f"Your OTP is {otp}",
        }
    )
    return responseData["messages"][0]["status"] == "0"


class CustomerAuth(Auth):
    """
    CustomerAuth class to interact with the authentication database
    for the customer user
    """

    def register_user(self, **kwargs):
        """Regitsers a Customer"""
        phone_no = kwargs.get("phone_no")
        try:
            customer = storage.find_user_by(Customer, phone_no=phone_no)
            if customer:
                raise ValueError(f"Phone_no {customer.phone_no} already exists")
        except NoResultFound:
            otp = self.generate_otp(phone_no)
            if otp:
                new_customer = Customer(**kwargs)
                new_customer.OTP = otp
                new_customer.save()
                return new_customer
            raise ValueError("Faild to generate otp")

    def valid_login(self, phone_no: str) -> bool:
        """validated a customer"""
        try:
            storage.find_user_by(Customer, phone_no=phone_no)
            return True
        except NoResultFound:
            return False

    def create_session_token(self, phone_no: str) -> Union[str, None]:
        """creates a session token"""
        try:
            user = storage.find_user_by(Customer, phone_no=phone_no)
        except NoResultFound:
            return None

        access_token = create_access_token(identity=user.phone_no)
        return access_token

    def generate_otp(self, phone_no: str) -> Any:
        """generates opt"""
        otp = _create_otp()
        if _send_otp(phone_no, otp):
            return otp
        return None
