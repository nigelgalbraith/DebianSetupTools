# DebianSetupSuite

DebianSetupSuite is a modular collection of setup tools for Debian-based systems.

It automates common configuration tasks like installing packages, enabling services, applying firewall presets, managing Docker, installing archives, and more — all driven by reusable modules plus per-tool constants and JSON config.

The goal is simple:

- keep tools modular
- keep logic reusable
- keep execution predictable
- avoid large one-off scripts

---

## What It Does

Depending on the selected tool (constants module) and config, DebianSetupSuite can:

- Check and install required dependencies
- Install or remove APT packages
- Install `.deb` packages
- Install Flatpak applications
- Install from archives (and manage extracted apps)
- Configure UFW firewall presets
- Enable/disable/verify systemd services
- Manage Docker-related operations (depending on constants)
- Apply machine/profile-based configuration from JSON

The execution style is consistent:

1. Detect host/model identity
2. Resolve the correct config file from a primary config map
3. Validate config structure (primary + optional secondary validation)
4. Compute job status (installed/uninstalled)
5. Build an action plan
6. Confirm (or auto-confirm)
7. Execute a defined set of steps (“pipeline states”)
8. Print a summary + write logs

---

## How It Works

### Constants Modules

Each “tool” is defined by a constants module (examples in `constants/`), which specifies things like:

- which JSON config to load
- what keys and required fields the config must contain
- dependencies to check/install
- what actions exist (`ACTIONS`)
- what steps to run for each action (`PIPELINE_STATES`)
- labels and plan display columns
- logging settings

Examples:

- `constants.PackageConstants`
- `constants.DebConstants`
- `constants.FlatpakConstants`
- `constants.ThirdPartyConstants`
- `constants.ArchiveConstants`
- `constants.DockerConstants`
- `constants.FirewallConstants`
- `constants.StartupServicesConstants`
- `constants.ShutdownServicesConstants`
- `constants.NetworkConstants`
- (and others in the repo)

### The Loader

`DebianLoader.py` is the entrypoint.

It loads the selected constants module, detects system identity (host/model), resolves the correct JSON config, validates it, builds actions, and executes the selected action.

---

## Run

### Basic

```bash
python3 DebianLoader.py
```

If a tool requires root, run it with sudo (your constants decide this via `REQUIRED_USER`):

```bash
sudo python3 DebianLoader.py
```

---

## CLI Arguments (Supported)

The loader supports the following flags (implemented in `modules/state_machine_utils.py`):

- `--constants`
  Select which constants module to run (tool selection).
- `--status`
  Show installed/uninstalled status summary and exit (no changes).
- `--action <ACTION_NAME>`
  Run an action directly (non-menu selection).
- `--targets job1,job2,job3`
  Comma-separated list of job names to operate on (used with `--action`).
- `--plan-only`
  Print the execution plan and exit without making changes.
- `--yes` / `-y`
  Auto-confirm prompts (useful for non-interactive runs).

---

## Usage Examples

### 1) Pick a tool via constants module

```bash
python3 DebianLoader.py --constants constants.PackageConstants
```

### 2) Show status only

```bash
python3 DebianLoader.py --constants constants.PackageConstants --status
```

### 3) Print the plan only (no changes)

```bash
python3 DebianLoader.py --constants constants.PackageConstants --action Install --plan-only
```

### 4) Run an action against specific targets

```bash
python3 DebianLoader.py --constants constants.PackageConstants --action Install --targets "curl,wget"
```

### 5) Auto-confirm prompts

```bash
python3 DebianLoader.py --constants constants.PackageConstants --action Install --targets "curl,wget" --yes
```

> Note: `--action` choices are generated dynamically from the selected constants module’s `ACTIONS` keys.

---

## Configuration Resolution

The loader resolves config based on identity detection:

- Detects host + model
- Looks up a config path in the “primary config” mapping
- Prefers host override (if present)
- Falls back to model
- Falls back to a default identity key (defined in the detection config)

If the resolved config fails validation, the loader prints a verification report and exits.

---

## Logging

Logs are written to a log directory defined by constants.

The loader:

- creates timestamped log files
- writes console output to logs
- rotates logs based on `LOGS_TO_KEEP`
- prints the final log file path at the end of a run

---

## Design Principles

This repo is built around:

- configuration-driven behaviour (JSON controls what happens)
- small modules that do one thing
- predictable execution flow
- explicit validation before changes

---


## License

MIT License.

Anyone is free to use, modify, distribute, or improve this code.

## License
MIT License.

Anyone is free to use, modify, distribute, or improve this code.
