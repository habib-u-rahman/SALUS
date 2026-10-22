"""Record vital sign/lab readings (nurse) and FHIR intake endpoint.

Belongs to: Module 1 Data Intake.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/observations", tags=["observations"])
