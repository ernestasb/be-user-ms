"""
Module containing the routes authorization
"""
import logging

from fastapi import APIRouter, Depends, status
from src.database import db_session
from src.crud.auth_crud import crud_login
from sqlalchemy.orm import Session
from src.security import SecurityManager
from src.schemas.auth_schema import TokenSchema, LoginSchema
from src.utils import respond


router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/login", response_model=TokenSchema, status_code=status.HTTP_200_OK)
async def login(request_body: LoginSchema, session: Session = Depends(db_session)):
    logging.info("REQUEST: login")
    response = await crud_login(session, request_body)
    logging.info("Login successful.")
    return response


@router.post("/", status_code=status.HTTP_200_OK)
async def authenticate(request_body: TokenSchema):
    logging.info("REQUEST: authenticate")
    await SecurityManager.authenticate(request_body.model_dump()["access_token"])
    logging.info("Authentication successful.")
    return respond(200, "User is authenticated succesfully.", "Authenticated", "info")
