"""Medicine list, RiskBridge results, and accept/keep-change endpoints.

Belongs to: Module 4 RiskBridge.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/medications", tags=["medications"])
