"""
Module containing the CRUD functions for the user model
"""

from sqlalchemy.orm import Session

from src.errors import CustomException
from src.security import SecurityManager
from src.models.user_model import User
from src.schemas.user_schema import UserChangePassword, UserCreate


async def crud_create_user(session: Session, schema: UserCreate):
    """CRUD function to create a new User

    Args:
        session (Session): database session
        schema (UserCreate): schema containing data

    Returns:
        User: User object which was created
    """
    # hashing password before save
    if session.query(User).filter_by(email=schema.email).first():
        raise CustomException(
            422,
            "Invalid email",
            "User with this email already exists.",
        )
    new_user = User(**schema.model_dump())
    new_user.password = SecurityManager.hash(hash_string=new_user.password)
    session.add(new_user)
    session.commit()
    return new_user


async def crud_change_password(session: Session, schema: UserChangePassword):
    """CRUD function to change the password of a User

    Args:
        session (Session): database session
        schema (UserChangePassword): schema containing data

    Raises:
        CustomException: When invalid password
        CustomException: When resource not found

    Returns:
        User: User object which was updated
    """
    if found := session.query(User).get(schema.id):
        if SecurityManager.compare_hash(found.password, schema.old_password):
            found.password = SecurityManager.hash(hash_string=schema.new_password)
            session.commit()
            return found
        else:
            raise CustomException(
                422,
                "Invalid password",
                "Old password does not match with the current one.",
            )
    raise CustomException(
        200, "Resource not found", f"User with ID {schema.id} not found."
    )


async def crud_get_all_users(session: Session):
    """CRUD function to get all User data

    Args:
        session (Session): database session

    Returns:
        List[User]: List of all users
    """
    return session.query(User).all()


async def crud_get_user_by_id(session: Session, user_id: int):
    """CRUD function to get User data by ID

    Args:
        session (Session): database session
        user_id (int): ID of user to get

    Raises:
        CustomException: When resource not found

    Returns:
        User: User object which was fetched
    """
    if response := session.query(User).get(user_id):
        return response
    raise CustomException(
        200, "Resource not found", f"User with ID:{user_id} not found."
    )


async def crud_update_user(session: Session, user_id: int, schema: UserCreate):
    """CRUD function to update User data

    Args:
        session (Session): database session
        user_id (int): ID of user to update
        schema (UserCreate): schema containing data

    Raises:
        CustomException: When resource not found

    Returns:
        User: User object which was updated
    """
    if found := session.query(User).get(user_id):
        for field, value in schema.model_dump(exclude_unset=True).items():
            setattr(found, field, value)
        session.commit()
        return found
    raise CustomException(
        200, "Resource not found", f"User with ID {user_id} not found."
    )
