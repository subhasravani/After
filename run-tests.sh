#!/usr/bin/env bash
set -euxo pipefail

apt-get update
apt-get install -y --no-install-recommends python3 python3-venv python3-pip
python3 -m pip install --upgrade pip
pip3 install pytest

TEST_DIR="${TEST_DIR:-/tests}"
PYTHONPATH="$TEST_DIR" pytest -q "$TEST_DIR"
