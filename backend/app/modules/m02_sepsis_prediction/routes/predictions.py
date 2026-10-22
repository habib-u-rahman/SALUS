"""Endpoint to fetch sepsis risk prediction for a patient.

Belongs to: Module 2 Sepsis Prediction.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/predictions", tags=["predictions"])
