"""
Module containing all the extensions used in the application
"""

import datetime
import hashlib
import sys

from dotenv import dotenv_values
import jwt

from src.errors import CustomException


env_values = dotenv_values(".env")
required_variables = [
    "DB_USER",
    "DB_PASSWORD",
    "DB_IP",
    "DB_NAME",
    "DB_TEST_NAME",
    "DB_PORT",
    "HASH_SALT",
    "SECRET_KEY",
    "ACCESS_TOKEN_EXPIRE_MINUTES",
]


class SecurityManager:
    """
    Class containing security related methods
    """

    @staticmethod
    def validate_env():
        """
        Function to validate the .env file
        """
        missing_variables = [var for var in required_variables if var not in env_values]

        if missing_variables:
            missing = list(missing_variables)
            print(f"ERROR: .env variables missing: {missing}")
            sys.exit(1)

    @staticmethod
    def hash(hash_string: str):
        """Function to hash a string

        Args:
            hash_string (str): String to be hashed

        Returns:
            str: Hashed string
        """
        return hashlib.md5(
            str(hash_string + env_values["HASH_SALT"]).encode()
        ).hexdigest()

    @staticmethod
    def compare_hash(hashed_string: str, hash_string: str):
        """Function to compare a hashed string with a string

        Args:
            hashed_string (str): Hashed string
            hash_string (str): String to be hashed

        Returns:
            bool: True if the strings match, False otherwise
        """
        if hashed_string == SecurityManager.hash(hash_string):
            return True
        return False

    @staticmethod
    def generate_jwt(
        user_dict: dict,
        expire: int = int(env_values["ACCESS_TOKEN_EXPIRE_MINUTES"]),
    ):
        """Function to generate a JWT token

        Args:
            user_dict (dict): User data dictionary
            expire (dict, optional): Time for token to expire.
            Defaults to {"minutes": int(env_values["ACCESS_TOKEN_EXPIRE_MINUTES"])}.

        Returns:
            str: JWT token
        """
        user_dict["exp"] = datetime.datetime.now(
            tz=datetime.timezone.utc
        ) + datetime.timedelta(minutes=expire)
        return jwt.encode(
            user_dict,
            env_values["SECRET_KEY"],
            algorithm="HS256",
        )

    @staticmethod
    async def authenticate(token: str):
        """Function to authenticate a JWT token

        Args:
            token (str): JWT token

        Returns:
            dict: Decoded JWT token
        """
        try:
            if jwt.decode(token, env_values["SECRET_KEY"], algorithms=["HS256"]):
                return jwt.decode(token, env_values["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError as exc:
            raise CustomException(
                401,
                "Token expired",
                "Token has expired, please login again.",
            ) from exc
        except jwt.InvalidTokenError as exc:
            raise CustomException(
                401,
                "Invalid token",
                "Token is invalid, please login again.",
            ) from exc
