"""
Module containing error handles for global handling
"""
from fastapi import Request  # pylint: disable=unused-argument
from sqlalchemy.exc import OperationalError, ProgrammingError

from src.utils import respond


class CustomException(Exception):
    """
    Custom exception class
    """

    def __init__(self, status_code: int, message: str, detail: str = None):
        """Constructor method

        Args:
            status_code (int): status code
            message (str): message
            detail (str): detail
        """
        self.status_code = status_code
        self.message = message
        self.detail = detail


async def custom_exc(
    request: Request, error: CustomException
):  # pylint: disable=unused-argument
    """Custom exception handler

    Args:
        request (Request): request
        error (CustomException): error

    Returns:
        JSONResponse: response
    """
    return respond(error.status_code, error.detail, error.message)


async def operational_error_exc(
    request: Request, error: OperationalError
):  # pylint: disable=unused-argument
    """Operational error handler

    Args:
        request (Request): request
        error (CustomException): error

    Returns:
        JSONResponse: response
    """
    if "Connection refused" in str(error.orig):
        return respond(503, str(type(error.orig)), str(error.orig))
    return respond(500, str(type(error.orig)), str(error.orig))


async def programming_error_exc(
    request: Request, error: ProgrammingError
):  # pylint: disable=unused-argument
    """Programming error handler

    Args:
        request (Request): request
        error (CustomException): error

    Returns:
        JSONResponse: response
    """
    return respond(503, str(type(error.orig)), str(error.orig))
