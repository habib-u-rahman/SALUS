"""Patient list, patient record, timeline, and replay mode endpoints.

Belongs to: Module 8 Doctor & Nurse Dashboard.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/patients", tags=["patients"])
