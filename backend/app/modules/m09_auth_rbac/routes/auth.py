"""Register, login, token refresh, verify email, and forgot/reset password endpoints.

Belongs to: Module 9 Login & Role-Based Access.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])
