"""Question-answering assistant endpoint backed by RAG.

Belongs to: Module 6 Plain-Language Reports & Assistant.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/assistant", tags=["assistant"])
