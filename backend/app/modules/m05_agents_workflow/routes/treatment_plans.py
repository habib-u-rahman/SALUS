"""View, approve, edit, or reject a treatment plan (doctor only).

Belongs to: Module 5 Multi-Agent Workflow.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/treatment-plans", tags=["treatment-plans"])
