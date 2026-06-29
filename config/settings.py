"""Project settings and Google Earth Engine initialization helpers.

This module holds environment-backed configuration for the GeoFlood Agent
project. It also provides a small helper for initializing Google Earth Engine
for either service-account-based automation or interactive local development.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import ee
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-backed configuration for the GeoFlood Agent project."""

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.example"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    gee_project: str = Field(default="")
    gee_service_account_key: str = Field(default="")
    openrouter_api_key: str = Field(default="")
    llm_model: str = Field(default="google/gemma-3-27b-it")
    data_dir: str = Field(default="./data")
    worldpop_path: str = Field(default="./data/worldpop/pak_ppp_2020_100m.tif")
    model_checkpoint: str = Field(default="MuhammadBilal0021/segformer-flood-sentinel")
    log_level: str = Field(default="INFO")


settings = Settings()


def _service_account_credentials_from_key_value(key_value: str) -> ee.ServiceAccountCredentials:
    """Build Earth Engine credentials from a JSON file path or raw JSON string."""

    key_path = Path(key_value).expanduser()
    if key_path.is_file():
        service_account_data = json.loads(key_path.read_text(encoding="utf-8"))
        client_email = service_account_data["client_email"]
        return ee.ServiceAccountCredentials(client_email, key_file=str(key_path))

    service_account_data = json.loads(key_value)
    client_email = service_account_data["client_email"]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as temp_file:
        json.dump(service_account_data, temp_file)
        temp_key_path = temp_file.name

    return ee.ServiceAccountCredentials(client_email, key_file=temp_key_path)


def init_gee() -> None:
    """Initialize Google Earth Engine for automated or interactive use."""

    project = settings.gee_project or None
    key_value = settings.gee_service_account_key.strip()

    if key_value:
        credentials = _service_account_credentials_from_key_value(key_value)
        ee.Initialize(credentials=credentials, project=project)
        return

    try:
        ee.Initialize(project=project)
    except Exception:
        ee.Authenticate()
        ee.Initialize(project=project)
