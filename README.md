DebianSetupSuite

DebianSetupSuite is a Python-based toolset for automating system setup on Debian-based systems.

It can handle tasks such as:
  Installing and removing packages
  Configuring firewall rules
  Managing services
  Running predefined system setup actions
  
The tools are driven by JSON configuration files. A shared loader handles validation, dependency checks, menu selection, and execution steps in a consistent way. 
Each action runs through a simple flow: validate → show plan → confirm → execute → report status.
The goal is straightforward: make system configuration repeatable and easier to manage.
