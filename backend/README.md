# SALUS Backend

FastAPI backend for SALUS, a patient safety platform (sepsis prediction,
RiskBridge medicine rechecking, multi-agent workflow, and role-based
dashboards for patient/doctor/nurse/admin).

## Setup

1. Create a virtual environment and install dependencies:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt -r requirements-dev.txt
   ```
2. Copy `.env.example` to `.env` and fill in real values.
3. Run database migrations: `alembic upgrade head`.
4. Start the API: `uvicorn app.main:app --reload`.
5. Check `http://127.0.0.1:8000/health`.

## Layout: one folder per proposal module

Each of the 10 proposal modules lives in its own folder under
`app/modules/`, containing its own `models/`, `schemas/`, `routes/`, and
module-specific logic. See `app/modules/README.md` for the full
module-to-folder table. Only genuinely shared infrastructure sits outside
`app/modules/`:

| Folder | Purpose |
|---|---|
| app/core | settings (config.py) and logging — not owned by any one module |
| app/db | SQLAlchemy base/session + Alembic migrations (one database, one migration chain) |
| app/api/deps.py | shared "current user" / "db session" dependencies used by every module's routes |
| app/scheduler | periodic background jobs that call into several modules |
| app/utils | small generic helpers |
| app/modules/m01_data_intake ... m10_admin | the 10 proposal modules, each self-contained |
| tests | pytest suite, mirroring the module folders |
