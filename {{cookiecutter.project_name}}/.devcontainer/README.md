# Devcontainer

Compose-based devcontainer that reuses `docker-compose.yml` and adds a `workspace` service with devcontainer features.

Use **Dev Containers: Open Folder in Container...** in VS Code to start.

## Workspace

- **Config**: `.devcontainer/devcontainer.json`
- **Dockerfile**: `.devcontainer/Dockerfile.workspace`
- **Workspace folder**: `/opt/code` inside the container

## Services

Started via `runServices` in `devcontainer.json`:
- `workspace` — development container

All services stop when VS Code is closed (`shutdownAction: stopCompose`).

## Features and Extensions

Devcontainer features (installed automatically):
- zsh + zsh-plugins
- node (for CLI tool installation)

VS Code extensions (installed automatically):
- `ms-python.python`
- `ms-python.debugpy`
- `ms-azuretools.vscode-docker`

## Volume Strategy

| Mount | Purpose |
|---|---|
| `{{cookiecutter.module_name}}_profile` → `/home/vscode` | Persists shell history, Claude Code auth, and other user-level state across rebuilds |
| Anonymous volume → `/home/vscode/.vscode-server` | Fresh VS Code server on each rebuild (avoids stale extension state) |
| `~/.claude` → `/mnt/claude` (read-only) | Host Claude config; synced to `~/.claude` on each start by `postStartCommand` |
| `~/.codex` → `/mnt/codex` (read-only) | Host Codex config; synced to `~/.codex` on each start by `postStartCommand` |
| `~/.config/opencode` → `/mnt/opencode-config` (read-only) | Host OpenCode global config; synced to `~/.config/opencode` on each start by `postStartCommand` |
| `~/.local/share/opencode/auth.json` → `/mnt/opencode-auth.json` (read-only) | Host OpenCode auth storage; synced to `~/.local/share/opencode/auth.json` on each start by `postStartCommand` |
| `~/.screenshots` → `/tmp/screenshots` (read-only) | Host screenshots accessible inside the container |

## Personal Configuration

Host-specific mounts (e.g. git config includes) are kept in a gitignored `docker-compose.personal.yml`.

On first open, `initializeCommand` copies `docker-compose.personal.yml.example` → `docker-compose.personal.yml`. Edit the personal file to add your own bind mounts or environment variables.

AI tooling is configured there as well:
- `INSTALL_CLAUDE` (`true`/`false`) — enables or disables Claude Code installation in post-create.
- `INSTALL_CODEX` (`true`/`false`) — enables or disables OpenAI Codex CLI installation in post-create.
- `INSTALL_OPENCODE` (`true`/`false`) — enables or disables OpenCode installation in post-create.
- `CLAUDE_MARKETPLACES` — space- or comma-separated marketplace sources to add before plugin installation.
- `CLAUDE_PLUGINS` — space- or comma-separated plugin list for auto-install.

## Lifecycle Hooks

| Hook | What it does |
|---|---|
| `initializeCommand` | Runs `.devcontainer/scripts/host-initialize.sh` on host: ensures `~/.claude`, `~/.codex`, `~/.config/opencode`, `~/.local/share/opencode`, and `~/.screenshots` paths exist, copies `docker-compose.personal.yml` from template if missing, and bootstraps `.vscode/launch.json` from `.devcontainer/launch.json` |
| `postCreateCommand` | Runs `.devcontainer/scripts/post-create.sh`: installs Claude Code CLI, Codex CLI, and OpenCode when enabled, adds requested Claude marketplaces, then installs requested plugins |
| `postStartCommand` | Runs `.devcontainer/scripts/post-start.sh`: syncs Claude, Codex, and OpenCode configs from read-only mounts (`/mnt/claude`, `/mnt/codex`, `/mnt/opencode-*`) into writable home directories |

All scripts support local overrides via `<script-name>.local.sh` (e.g. `post-create.local.sh`), which are sourced at the end if present.

## Claude Plugins

Plugin setup is env-driven via `docker-compose.personal.yml`.

Defaults from `.devcontainer/docker-compose.personal.yml.example`:
- `INSTALL_CLAUDE: "true"`
- `INSTALL_CODEX: "true"`
- `INSTALL_OPENCODE: "true"`
- `CLAUDE_MARKETPLACES: "umputun/cc-thingz"`
- `CLAUDE_PLUGINS: "code-simplifier,brainstorm@umputun-cc-thingz,planning@umputun-cc-thingz,thinking-tools@umputun-cc-thingz,skill-eval@umputun-cc-thingz,workflow@umputun-cc-thingz"`

To customize, update your personal override:

```yaml
CLAUDE_MARKETPLACES: "https://example.com/marketplace.json,github.com/org/repo"
CLAUDE_PLUGINS: "code-simplifier,another-plugin"
```
