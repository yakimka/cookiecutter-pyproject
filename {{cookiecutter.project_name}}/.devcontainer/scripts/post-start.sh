#!/usr/bin/env bash
# Syncs agent configuration files from read-only mounts (/mnt/{claude,codex})
# into writable home directories (~/.claude, ~/.codex).
# Runs on every container start via postStartCommand.
set -euo pipefail

HOME_DIR="${HOME:-/home/vscode}"

# sync_path <source> <target>
# Copies a file or non-empty directory from source to target.
sync_path() {
    local src="$1" dst="$2"
    if [ -f "$src" ]; then
        mkdir -p "$(dirname "$dst")"
        cp -a "$src" "$dst"
    elif [ -d "$src" ] && [ -n "$(ls -A "$src" 2>/dev/null)" ]; then
        rm -rf "$dst"
        cp -a "$src" "$dst"
    else
        return 0
    fi
    echo "Synced $src -> $dst"
}

# Claude configs
echo "Syncing claude configuration files..."
mkdir -p "${HOME_DIR}/.claude"
sync_path "/mnt/claude/CLAUDE.md"       "${HOME_DIR}/.claude/CLAUDE.md"
# sync_path "/mnt/claude/.credentials.json" "${HOME_DIR}/.claude/.credentials.json"
sync_path "/mnt/claude/skills"          "${HOME_DIR}/.claude/skills"
sync_path "/mnt/claude/agents"          "${HOME_DIR}/.claude/agents"
sync_path "/mnt/claude/instructions"    "${HOME_DIR}/.claude/instructions"
sync_path "/mnt/claude/prompts"         "${HOME_DIR}/.claude/prompts"
sync_path "/mnt/claude/commands"        "${HOME_DIR}/.claude/commands"
sync_path "/mnt/claude/rules"           "${HOME_DIR}/.claude/rules"
sync_path "/mnt/claude/hooks"           "${HOME_DIR}/.claude/hooks"

# Codex configs
echo "Syncing codex configuration files..."
mkdir -p "${HOME_DIR}/.codex"
sync_path "/mnt/codex/auth.json"        "${HOME_DIR}/.codex/auth.json"

echo "Agent config sync complete."

# Run local overrides if present
LOCAL_SCRIPT="$(dirname "${BASH_SOURCE[0]}")/post-start.local.sh"
if [ -f "$LOCAL_SCRIPT" ]; then
    echo "Running local overrides from $LOCAL_SCRIPT..."
    source "$LOCAL_SCRIPT" || echo "Warning: $LOCAL_SCRIPT exited with status $?" >&2
fi
