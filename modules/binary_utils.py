#!/usr/bin/env python3
"""
binary_utils.py

Utilities for managing binary installations.
"""

import subprocess
from pathlib import Path

# ---------------------------------------------------------------------
# BINARY STATUS CHECK
# ---------------------------------------------------------------------
def check_binary_status(path: str) -> bool:
    """Return True if binary exists."""
    return Path(path).expanduser().exists()

# ---------------------------------------------------------------------
# BINARY INSTALLATION HELPERS
# ---------------------------------------------------------------------

def install_binary(binary_path: str, install_path: str) -> bool:
    """Move binary to install path and make executable."""
    try:
        src = Path(binary_path)
        dest = Path(install_path).expanduser()
        if not src.exists():
            print(f"[install_binary] Source not found: {src}")
            return False
        # Move binary
        rc = subprocess.run(
            ["sudo", "mv", str(src), str(dest)],
            check=False
        ).returncode
        if rc != 0:
            return False
        # Make executable
        rc = subprocess.run(
            ["sudo", "chmod", "a+rx", str(dest)],
            check=False
        ).returncode
        return rc == 0
    except Exception as e:
        print(f"[install_binary] Error: {e}")
        return False


def uninstall_binary(install_path: str) -> bool:
    """Remove installed binary."""
    try:
        path = Path(install_path).expanduser()
        if not path.exists():
            return True
        return subprocess.run(
            ["sudo", "rm", "-f", str(path)],
            check=False
        ).returncode == 0
    except Exception as e:
        print(f"[uninstall_binary] Error: {e}")
        return False