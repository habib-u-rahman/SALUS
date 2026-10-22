"""Server-side role checks used as FastAPI dependencies, e.g. require_role('doctor'), so nurses/patients cannot call doctor-only endpoints even if the UI is bypassed. Imported by every other module's routes.

Belongs to: Module 9 Login & Role-Based Access.
"""

def require_role(*allowed_roles: str):
    """Return a FastAPI dependency that only allows the given roles through."""
    pass
