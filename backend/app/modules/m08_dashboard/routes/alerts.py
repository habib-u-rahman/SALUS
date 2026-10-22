"""List alerts, view details, acknowledge, and escalate endpoints.

Belongs to: Module 8 Doctor & Nurse Dashboard.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/alerts", tags=["alerts"])
