"""Dependencies for dependency injection in routes module."""


from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from jose import ExpiredSignatureError, jwt

from agenda_back.common.config import settings
from agenda_back.common.enums import TokenTypes
from agenda_back.common.exceptions import TokenTypeError
from agenda_back.common.logger import log
from agenda_back.helpers import auth_helpers
from agenda_back.schemas.v1.common_schemas import PaginationSchema
from agenda_back.schemas.v1.user_schemas import CurrentUser


def paginate(req: Request) -> PaginationSchema:
    """Dependency for requested data pagination."""
    return PaginationSchema(
        offset=req.query_params.get("offset"),
        limit=req.query_params.get("limit"),
        sort=req.query_params.get("sort"),
        order=req.query_params.get("order"),
    )


def authenticate(
    header: HTTPAuthorizationCredentials=Depends(HTTPBearer())
) -> CurrentUser:
    """Dependency for user authentication."""
    try:
        credentials = jwt.decode(
            header.credentials,
            settings.JWT_SECRET_KEY,
            algorithms=settings.JWT_ALGORITHM,
        )
        auth_helpers.validate_token_type(
            TokenTypes.AUTH,
            credentials["type"],
        )
        return CurrentUser(
            id=credentials.get("id"),
            username=credentials.get("username"),
            first_name=credentials.get("first_name"),
            last_name=credentials.get("last_name"),
            role_id=credentials.get("role_id"),
            role_name=credentials.get("role_name"),
            market_id=credentials.get("market_id"),
            exp=credentials.get("exp"),
        )
    except TokenTypeError as e:
        error = f"[Error]: {e}"
    except ExpiredSignatureError:
        error = "[Error]: Token expired, login again to generate a new one."
    except Exception as e:
        log.error(f"[Error]: {e}")
        error = "[Error]: Invalid token."
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"error": error}
    )
