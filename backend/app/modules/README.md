# app/modules — one folder per proposal module

Each folder below is self-contained: its own `models/` (SQLAlchemy tables),
`schemas/` (Pydantic request/response shapes), `routes/` (FastAPI
endpoints), and any module-specific business logic. Shared infrastructure
(database session/base, settings, the scheduler, generic helpers) lives in
`app/core`, `app/db`, `app/scheduler`, `app/utils` instead, since it isn't
owned by a single module.

| Folder | Proposal module | What lives here |
|---|---|---|
| `m01_data_intake` | 1. Data Intake | vital sign/lab observations, FHIR conversion + validation, the synthetic patient data generator |
| `m02_sepsis_prediction` | 2. Sepsis Prediction | the LSTM sepsis model, baseline models, feature engineering, prediction records |
| `m03_prescription_recognition` | 3. Prescription & Medicine Recognition | prescription image uploads, OCR, pill/box recognition |
| `m04_riskbridge` | 4. RiskBridge (our main contribution) | kidney/liver clearance estimates, dosing rules, the recheck engine, alternative suggestions, rating history, and the external drug-data clients it depends on |
| `m05_agents_workflow` | 5. Multi-Agent Workflow | the LangGraph state/graph/LLM wiring, all 10 agents, and treatment plans |
| `m06_assistant_rag` | 6. Plain-Language Reports & Assistant | the RAG pipeline (ingest/retrieve/prompts) behind the question-answering assistant |
| `m07_patient_portal` | 7. Patient Portal | dose reminders, family member links, the patient-facing portal endpoints |
| `m08_dashboard` | 8. Doctor & Nurse Dashboard | patients/wards/beds, resources, alerts, nurse tasks, realtime WebSocket push, notifications |
| `m09_auth_rbac` | 9. Login & Role-Based Access | users, password hashing, JWT, server-side role checks, login rate limiting |
| `m10_admin` | 10. Admin Panel | admin-editable settings, the audit log |

Cross-module imports are expected and fine — e.g. every module's `routes/`
depends on `m09_auth_rbac`'s role-check dependency to protect its
endpoints. What this layout avoids is the opposite problem: having to open
five unrelated top-level folders just to see everything about one module.
