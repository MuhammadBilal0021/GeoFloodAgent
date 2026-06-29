"""FastAPI application scaffold for the GeoFlood Agent API.

This module only defines the application object that Uvicorn expects. Route
implementation belongs here later, but no endpoints are included in this setup.
"""

from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="GeoFlood Agent API", version="0.1.0")
