# DebianSetupSuite

DebianSetupSuite is a modular collection of setup tools for Debian-based systems.

It automates common system configuration tasks such as package installation, firewall rules, service management, and application deployment.

The goal is simple:
- keep tools modular
- keep logic reusable
- keep execution predictable
- avoid large one-off scripts

---

## What It Does

Depending on the selected tool and configuration, DebianSetupSuite can:

- Check and install required dependencies
- Install or remove APT packages
- Install `.deb` packages
- Install Flatpak applications
- Configure UFW firewall rules
- Enable, disable, or verify systemd services
- Apply machine/profile-based configurations from JSON

Each operation follows the same execution flow:

1. Pre-validation
2. Plan display (what will happen)
3. Confirmation
4. Execution
5. Status reporting

This keeps behaviour consistent across all tools.

---

## How It Works

Each tool is defined through a **constants module**, which specifies:

- Config path
- Validation rules
- Dependencies
- Available actions
- Pipeline steps (pre and exec phases)

The loader (`DebianLoader.py`) handles:

- Dependency checking
- Config loading and validation
- Status summary
- Menu selection
- Pipeline execution

Execution logic is separated from configuration, so behaviour is controlled by structured JSON rather than hardcoded logic.

---

## Run

Interactive mode:

```bash
sudo python3 DebianLoader.py
python3 DebianLoader.py
