"""Shared constants for geospatial processing and flood assessment scaffolding."""

from __future__ import annotations

SENTINEL_2_RGB_BANDS = {"R": 3, "G": 2, "B": 1, "NIR": 7}
SENTINEL_1_POLARIZATION_BANDS = ["VV", "VH"]
TARGET_CRS = "EPSG:4326"
SEN1FLOODS11_CLASS_MAP = {0: "no_flood", 1: "flood", 255: "no_data"}
DEFAULT_TILE_SIZE = 512
DEFAULT_OVERLAP = 64
