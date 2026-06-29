#!/usr/bin/env bash
set -euo pipefail

export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y --no-install-recommends \
  gdal-bin \
  libgdal-dev \
  libgeos-dev \
  libproj-dev \
  libspatialindex-dev \
  python3-gdal \
  build-essential \
  libffi-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  weasyprint \
  fonts-liberation

export GDAL_VERSION="$(gdal-config --version)"
export CPLUS_INCLUDE_PATH="/usr/include/gdal"
export C_INCLUDE_PATH="/usr/include/gdal"

python -m pip install --upgrade pip setuptools wheel
python -m pip install --no-cache-dir "GDAL==${GDAL_VERSION}"
python -m pip install --no-cache-dir -r requirements.txt
