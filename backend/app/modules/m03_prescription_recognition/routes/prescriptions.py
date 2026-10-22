"""Upload prescription image, run OCR/pill recognition, and confirm results.

Belongs to: Module 3 Prescription & Medicine Recognition.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/prescriptions", tags=["prescriptions"])
