#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Card News Skill: Environment Setup ==="

# Create Python virtual environment
if [ ! -d ".venv" ]; then
    echo "[1/3] Creating Python virtual environment..."
    python3 -m venv .venv
else
    echo "[1/3] Virtual environment already exists, skipping..."
fi

# Activate and install dependencies
echo "[2/3] Installing Python dependencies..."
source .venv/bin/activate
pip install --quiet -r requirements.txt

# Install Playwright browser
echo "[3/3] Installing Chromium for Playwright..."
playwright install chromium

echo ""
echo "=== Setup complete! ==="
echo "To activate: source $SCRIPT_DIR/.venv/bin/activate"
