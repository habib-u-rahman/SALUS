"""Application entry point: creates the FastAPI app, wires up CORS, registers
every API router, sets up startup/shutdown hooks, and exposes GET /health.

Belongs to: all modules (this is the composition root that wires the whole
backend together). Each router is imported from its own module folder
under app/modules/ rather than a shared routes package.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.modules.m09_auth_rbac.routes.auth import router as auth_router
from app.modules.m09_auth_rbac.routes.users import router as users_router
from app.modules.m10_admin.routes.admin import router as admin_router
from app.modules.m08_dashboard.routes.patients import router as patients_router
from app.modules.m01_data_intake.routes.observations import router as observations_router
from app.modules.m02_sepsis_prediction.routes.predictions import router as predictions_router
from app.modules.m08_dashboard.routes.alerts import router as alerts_router
from app.modules.m04_riskbridge.routes.medications import router as medications_router
from app.modules.m05_agents_workflow.routes.treatment_plans import router as treatment_plans_router
from app.modules.m03_prescription_recognition.routes.prescriptions import router as prescriptions_router
from app.modules.m06_assistant_rag.routes.assistant import router as assistant_router
from app.modules.m07_patient_portal.routes.portal import router as portal_router
from app.modules.m08_dashboard.routes.tasks import router as tasks_router

app = FastAPI(title="SALUS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(admin_router)
app.include_router(patients_router)
app.include_router(observations_router)
app.include_router(predictions_router)
app.include_router(alerts_router)
app.include_router(medications_router)
app.include_router(treatment_plans_router)
app.include_router(prescriptions_router)
app.include_router(assistant_router)
app.include_router(portal_router)
app.include_router(tasks_router)


@app.on_event("startup")
async def on_startup():
    """Placeholder startup hook (DB connections, scheduler, model loading)."""
    pass


@app.on_event("shutdown")
async def on_shutdown():
    """Placeholder shutdown hook (close DB connections, stop scheduler)."""
    pass


@app.get("/health")
async def health():
    return {"status": "ok"}
