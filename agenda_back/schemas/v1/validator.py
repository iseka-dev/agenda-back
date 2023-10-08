"""Module with a pydantic validator schema implementation."""

import re

from pydantic import BaseModel


class ValidatorSchema(BaseModel):
    """
    Schema for field and data validation.

    Included validation:
    - Phone validation format
    - Zip Code validation format
    - Required field validation
    - password format validations
    """

    @staticmethod
    def phone_validation(v: int | str) -> int | str:
        if v:
            v_digits = re.sub("\\D", "", v)
            if len(v_digits) != 10:
                raise ValueError("Invalid phone number.")
            v = f"({v_digits[0:3]}) {v_digits[3:6]}-{v_digits[6:]}"
        return v

    @staticmethod
    def zip_code_validation(value: int | str) -> int | str:
        if value:
            v_digits = re.sub("\\D", "", value)
            total = len(v_digits)
            if total not in (5, 9):
                raise ValueError("Invalid ZIP code.")
            value = v_digits
        return value

    @staticmethod
    def required_field(value: int | str) -> int | str:
        if not value:
            raise ValueError("Missing required field.")
        return value

    @staticmethod
    def password_validation(value: int | str) -> int | str:
        if value and len(value) < 8:
            raise ValueError(
                "Password too short, 8 characters minimun."
            )
        return value
