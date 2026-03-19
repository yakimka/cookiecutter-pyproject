#!/usr/bin/env bash
set -euo pipefail

INSTALL_CLAUDE="${INSTALL_CLAUDE:-true}"
INSTALL_CODEX="${INSTALL_CODEX:-true}"
CLAUDE_MARKETPLACES="${CLAUDE_MARKETPLACES:-}"
CLAUDE_PLUGINS="${CLAUDE_PLUGINS:-}"

is_truthy() {
    case "${1,,}" in
    1 | true | yes | on)
        return 0
        ;;
    *)
        return 1
        ;;
    esac
}

# 1. Install Claude Code CLI (persists in named volume), if enabled.
if is_truthy "${INSTALL_CLAUDE}"; then
    if ! command -v claude &>/dev/null; then
        curl -fsSL https://claude.ai/install.sh | bash
    fi
else
    echo "Skipping Claude Code install (INSTALL_CLAUDE=${INSTALL_CLAUDE})"
fi

# 2. Install OpenAI Codex CLI (persists in named volume), if enabled.
if is_truthy "${INSTALL_CODEX}"; then
    if ! command -v codex &>/dev/null; then
        npm install -g @openai/codex
    fi
else
    echo "Skipping Codex install (INSTALL_CODEX=${INSTALL_CODEX})"
fi

# 3. Add Claude marketplaces and plugins (space- or comma-separated lists).
# ensure_claude_items <item_type> <list_cmd> <add_cmd> <items_csv>
# Idempotently adds Claude CLI items (marketplaces or plugins).
ensure_claude_items() {
    local item_type="$1" list_cmd="$2" add_cmd="$3" items_csv="$4"
    local -a items
    local -a list_args add_args
    read -r -a items <<<"${items_csv//,/ }"
    read -r -a list_args <<<"${list_cmd}"
    read -r -a add_args <<<"${add_cmd}"

    if [ "${#items[@]}" -eq 0 ]; then
        echo "No Claude ${item_type}s requested"
        return
    fi

    local existing
    existing="$(claude plugins "${list_args[@]}" 2>/dev/null || true)"
    for item in "${items[@]}"; do
        if grep -Fq "${item}" <<<"${existing}"; then
            echo "Claude ${item_type} '${item}' already present"
        elif claude plugins "${add_args[@]}" "${item}"; then
            echo "Added Claude ${item_type} '${item}'"
        else
            echo "Warning: failed to add Claude ${item_type} '${item}'" >&2
        fi
    done
}

if command -v claude &>/dev/null; then
    ensure_claude_items "marketplace" "marketplace list" "marketplace add" "${CLAUDE_MARKETPLACES}"
    ensure_claude_items "plugin" "list" "install" "${CLAUDE_PLUGINS}"
fi

# Run local overrides if present
LOCAL_SCRIPT="$(dirname "${BASH_SOURCE[0]}")/post-create.local.sh"
if [ -f "$LOCAL_SCRIPT" ]; then
    echo "Running local overrides from $LOCAL_SCRIPT..."
    source "$LOCAL_SCRIPT" || echo "Warning: $LOCAL_SCRIPT exited with status $?" >&2
fi
