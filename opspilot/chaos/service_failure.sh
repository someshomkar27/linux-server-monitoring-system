#!/usr/bin/env bash
set -euo pipefail
echo "Lab-only failure simulation; no real service is modified."
mkdir -p data
printf "FAILED
" > data/demo_service_state.txt
