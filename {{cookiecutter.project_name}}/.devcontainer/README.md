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
- `postgres`
- `valhalla`

All services stop when VS Code is closed (`shutdownAction: stopCompose`).

## Features and Extensions

Devcontainer features (installed automatically):
- zsh + zsh-plugins

VS Code extensions (installed automatically):
- `anthropic.claude-code`
- `ms-python.python`
- `ms-python.debugpy`
- `ms-azuretools.vscode-docker`

## Volume Strategy

| Mount | Purpose |
|---|---|
| `{{cookiecutter.module_name}}_profile` → `/home/vscode` | Persists shell history, Claude Code auth, and other user-level state across rebuilds |
| Anonymous volume → `/home/vscode/.vscode-server` | Fresh VS Code server on each rebuild (avoids stale extension state) |
| `~/.claude/CLAUDE.md` → `/home/vscode/.claude/CLAUDE.md` (read-only) | Shared global Claude instructions across projects |
| `~/.claude/{skills,agents,instructions,prompts,commands}` → `/home/vscode/.claude/...` (read-only) | Shared global Claude knowledge artifacts across projects |

## Personal Configuration

Host-specific mounts (e.g. git config includes) are kept in a gitignored `docker-compose.personal.yml`.

On first open, `initializeCommand` copies `docker-compose.personal.yml.example` → `docker-compose.personal.yml`. Edit the personal file to add your own bind mounts or environment variables.

Claude behavior is configured there as well:
- `INSTALL_CLAUDE` (`true`/`false`) — enables or disables Claude Code installation in post-create.
- `CLAUDE_MARKETPLACES` — space- or comma-separated marketplace sources to add before plugin installation.
- `CLAUDE_PLUGINS` — space- or comma-separated plugin list for auto-install.

## Lifecycle Hooks

| Hook | What it does |
|---|---|
| `initializeCommand` | Runs `.devcontainer/scripts/host-initialize.sh` on host: ensures `~/.claude` knowledge paths exist, copies `docker-compose.personal.yml` from template if missing, and bootstraps `.vscode/launch.json` from `.devcontainer/launch.json` |
| `postCreateCommand` | Runs `.devcontainer/scripts/post-create.sh`: reads `INSTALL_CLAUDE`, `CLAUDE_MARKETPLACES`, and `CLAUDE_PLUGINS`; installs Claude Code CLI when enabled, adds requested marketplaces, then installs requested plugins when `claude` command is available |

## Claude Plugins

Plugin setup is env-driven via `docker-compose.personal.yml`.

Defaults from `.devcontainer/docker-compose.personal.yml.example`:
- `INSTALL_CLAUDE: "true"`
- `CLAUDE_MARKETPLACES: ""`
- `CLAUDE_PLUGINS: "code-simplifier"`

To add marketplaces and plugins, update your personal override:

```bash
CLAUDE_MARKETPLACES: "https://example.com/marketplace.json,github.com/org/repo"
CLAUDE_PLUGINS: "code-simplifier,another-plugin"
```
