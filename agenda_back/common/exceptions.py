"""This module has the custom exceptions for the project."""

class InvalidCredentialsError(Exception):  # noqa: D101
    pass

class TokenNotFoundError(Exception):  # noqa: D101
    pass

class TokenTypeError(Exception):  # noqa: D101
    pass

class ExpiredSignatureError(Exception):  # noqa: D101
    pass
