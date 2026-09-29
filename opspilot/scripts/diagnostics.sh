#!/usr/bin/env bash
set -euo pipefail
echo "=== HOST ==="; hostnamectl 2>/dev/null || hostname
echo "=== UPTIME ==="; uptime
echo "=== MEMORY ==="; free -h
echo "=== DISK ==="; df -h /
echo "=== TOP PROCESSES ==="; ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 11
echo "=== NETWORK ==="; ss -tuln 2>/dev/null | head -n 20 || true
echo "=== FAILED SERVICES ==="; systemctl --failed --no-legend 2>/dev/null || true
