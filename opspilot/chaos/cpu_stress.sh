#!/usr/bin/env bash
set -euo pipefail
python3 -c 'import time; end=time.time()+10; x=0
while time.time()<end: x=(x+1)%1000003
print("CPU simulation complete")'
