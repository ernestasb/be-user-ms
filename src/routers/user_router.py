"""
Module containing the routes for the user model
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.crud.user_crud import (
    crud_create_user,
    crud_change_password,
    crud_get_user_by_id,
    crud_get_all_users,
    crud_update_user,
)
from src.database import db_session
from src.schemas.user_schema import UserCreate, UserGet, UserChangePassword, UserUpdate

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=UserGet, status_code=status.HTTP_201_CREATED)
async def crate_user(request_body: UserCreate, session: Session = Depends(db_session)):
    logging.info("REQUEST: create user")
    response = await crud_create_user(session, request_body)
    logging.info("User created successfully.")
    return response


@router.put("/change-password", response_model=UserGet, status_code=status.HTTP_200_OK)
async def patch_password(
    request_body: UserChangePassword, session: Session = Depends(db_session)
):
    logging.info("REQUEST: change password")
    response = await crud_change_password(session, request_body)
    logging.info("Password changed successfully.")
    return response


@router.get("/", response_model=List[UserGet], status_code=status.HTTP_200_OK)
async def get_all_users(session=Depends(db_session)):
    logging.info("REQUEST: change password")
    response = await crud_get_all_users(session)
    logging.info("Data fetched successfully.")
    return response


@router.get("/{user_id}", response_model=UserGet, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int, session=Depends(db_session)):
    logging.info("REQUEST: get user by ID")
    response = await crud_get_user_by_id(session, user_id)
    logging.info("Data fetched successfully.")
    return response


@router.put("/{user_id}", response_model=UserGet, status_code=status.HTTP_200_OK)
async def update_user(
    user_id: int, request_body: UserUpdate, session=Depends(db_session)
):
    logging.info("REQUEST: update user")
    response = await crud_update_user(session, user_id, request_body)
    logging.info("Data updated successfully.")
    return response
