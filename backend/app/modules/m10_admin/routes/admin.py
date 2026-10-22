"""Approve/reject staff, manage users & roles, wards & beds, view audit log and system settings/health.

Belongs to: Module 10 Admin Panel.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])
