"""
Authentication routes.

/login
/refresh-token
/set-password
/reset-password

"""

from fastapi import APIRouter, HTTPException, status
from jose import ExpiredSignatureError, JWTError

from agenda_back.common.exceptions import (
    InvalidCredentialsError,
    TokenNotFoundError,
    TokenTypeError,
)
from agenda_back.common.logger import log
from agenda_back.schemas.v1.auth_schemas import (
    LoginSchema,
    ResetPasswordRequestSchema,
    SetPasswordRequestSchema,
)
from agenda_back.services.v1.auth_service import AuthService
from agenda_back.services.v1.user_service import UserService

auth_routes = APIRouter(prefix="/v1/auth", tags=["authentication"])


@auth_routes.post("/login", status_code=status.HTTP_200_OK)
def login(data: LoginSchema) -> dict:
    """Login functionality."""
    try:
        return AuthService().login(data)
    except InvalidCredentialsError as e:
        code = status.HTTP_401_UNAUTHORIZED
        error = f"[Error]: {e}"
    except Exception as e:
        log.error(f"[Error]: {e}")
        code = status.HTTP_400_BAD_REQUEST
        error = "[Error]: Login failed."
    raise HTTPException(
        status_code=code,
        detail={"error": error},
    )


@auth_routes.post("/refresh-token", status_code=status.HTTP_200_OK)
async def refresh_token(refresh_token: str) -> str:
    """Get a new valid token."""
    try:
        return await AuthService().refresh_token(refresh_token)
    except TokenTypeError as e:
        error = f"[ERROR]: {e}"
    except ExpiredSignatureError:
        error = "[ERROR]: Session has finished, please login again."
    except JWTError:
        error = "[ERROR]: Invalid token signature, please login again."
    except Exception as e:
        log.error(f"[ERROR]: {e}")
        error = "[ERROR]: Invalid token, please login again."
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"error": error},
    )


@auth_routes.post("/set-password", status_code=status.HTTP_200_OK)
async def set_password(data: SetPasswordRequestSchema) -> any:
    """Set a password for the first time."""
    try:
        return await UserService().set_password(data)
    except TokenNotFoundError as e:
        code = status.HTTP_403_FORBIDDEN
        error = f"[ERROR]: {e}"
    except JWTError:
        code = status.HTTP_401_UNAUTHORIZED
        error = "[ERROR]: Invalid token, please try again with a new token."
    except TokenTypeError as e:
        code = status.HTTP_400_BAD_REQUEST
        error = f"[ERROR]: {e}"
    except Exception as e:
        log.error(f"[ERROR]: {e}")
        code = status.HTTP_400_BAD_REQUEST
        error = "[ERROR]: Password not set, please try again."
    raise HTTPException(status_code=code, detail={"error": error})


@auth_routes.put("/reset-password", status_code=status.HTTP_200_OK)
async def reset_password(data: ResetPasswordRequestSchema) -> any:
    """Set a new password."""
    try:
        return await UserService().reset_password(data)
    except Exception as e:
        log.error(f"[RARPE02]: {e}")
        error = "[RARPE02]: Password not reset, please try again."
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"error": error},
    )
