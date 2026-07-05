#!/bin/bash
set -euo pipefail
echo "Setting up Unit Test Generation Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
