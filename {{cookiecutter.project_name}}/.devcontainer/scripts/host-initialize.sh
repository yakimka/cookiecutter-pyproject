#!/usr/bin/env bash
# Runs on the HOST machine before the container is created.
set -euo pipefail

# Ensure agent config directories exist on the host for read-only bind mounts.
mkdir -p ~/.screenshots ~/.claude ~/.codex

# Copy personal compose override from template if missing
if [ ! -f .devcontainer/docker-compose.personal.yml ]; then
    cp .devcontainer/docker-compose.personal.yml.example \
       .devcontainer/docker-compose.personal.yml
fi

# Copy launch.json if missing
if [ ! -f .vscode/launch.json ]; then
    mkdir -p .vscode
    cp .devcontainer/launch.json .vscode/launch.json
fi

# Run local overrides if present
LOCAL_SCRIPT="$(dirname "${BASH_SOURCE[0]}")/host-initialize.local.sh"
if [ -f "$LOCAL_SCRIPT" ]; then
    echo "Running local overrides from $LOCAL_SCRIPT..."
    source "$LOCAL_SCRIPT" || echo "Warning: $LOCAL_SCRIPT exited with status $?" >&2
fi
