"""Container package for the 10 proposal modules.

Each sub-package (m01_data_intake, m02_sepsis_prediction, ...) is a
self-contained vertical slice: its own models, schemas, routes, and
business logic. Shared infrastructure (db session, core config, the
scheduler, generic utils) lives one level up in app/, not here.
"""
