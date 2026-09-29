# OpsPilot — Linux Incident Detection & Auto-Remediation

A Linux DevOps/SRE lab that turns system signals into an incident lifecycle: Detect → Diagnose → Decide → Remediate → Verify → Record.

Safe lab scope: remediation is allow-listed and defaults to dry-run mode.

## Stack
Python, psutil, Bash, FastAPI, SQLite, Docker, GitHub Actions.

## Features
- CPU, memory, disk and load monitoring
- Incident persistence and status lifecycle
- Linux diagnostics and process inspection
- Safe allow-listed service remediation
- Post-remediation verification
- REST API and browser dashboard
- Controlled failure simulation
- Automated tests and CI
- Docker support

## Run
cd opspilot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.demo_incident
python -m api.main

Open http://127.0.0.1:8000.

## Operational flow
Linux host -> metrics -> threshold detection -> incident -> diagnosis -> remediation -> verification -> resolution history

The project deliberately does not claim Kubernetes, Jenkins, Prometheus, Grafana, ELK or Ansible as implemented technologies.
