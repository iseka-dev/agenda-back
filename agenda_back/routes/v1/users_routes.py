"""Routes to the users api."""

from sqlite3 import IntegrityError

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from agenda_back.common.logger import log
from agenda_back.db.database import get_db_session
from agenda_back.schemas.v1.common_schemas import IdOnlyResponse
from agenda_back.schemas.v1.user_schemas import CreateUserRequestSchema
from agenda_back.services.v1.user_service import UserService

users_routes = APIRouter(
    prefix="/v1/users",
    tags=["users"],
)

@users_routes.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create(
    data: CreateUserRequestSchema,
    db_session: Session = Depends(get_db_session),
) -> IdOnlyResponse:
    """Create user."""
    try:
        return UserService().create(data, db_session)
    except IntegrityError:
        error = "Users Error: The email address was already taken."
    except Exception as e:
        log.error(f"Error: {e}")
        error = "Users Error: User was not created, please try again."
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={"Error": error},
    )
