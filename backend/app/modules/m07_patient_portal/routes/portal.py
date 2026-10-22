"""Patient portal endpoints: combined medicine list, reminders, family links.

Belongs to: Module 7 Patient Portal.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/portal", tags=["portal"])
