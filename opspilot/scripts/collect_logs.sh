#!/usr/bin/env bash
set -euo pipefail
OUT="logs/incident-"$(date +%Y%m%d-%H%M%S); mkdir -p "$OUT"
dmesg --level=err,warn > "$OUT/dmesg.txt" 2>/dev/null || true
journalctl -p warning -n 200 > "$OUT/journal.txt" 2>/dev/null || true
cp /var/log/syslog "$OUT/syslog.txt" 2>/dev/null || true
echo "Collected logs in $OUT"
