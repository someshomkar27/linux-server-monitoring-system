import subprocess
from .config import load_config
from .storage import update_incident,now
def restart_service(i,service,dry_run=None):
    cfg=load_config()["remediation"]; dry_run=cfg["dry_run"] if dry_run is None else dry_run
    if service not in cfg["allowed_services"]: raise ValueError("Service is not allow-listed")
    if dry_run:
        action="DRY-RUN: would restart "+service; update_incident(i,action=action,status="REMEDIATION_SIMULATED")
        return {"success":True,"action":action}
    r=subprocess.run(["sudo","systemctl","restart",service],capture_output=True,text=True,timeout=20)
    if r.returncode:
        update_incident(i,action=r.stderr.strip(),status="REMEDIATION_FAILED"); return {"success":False,"action":r.stderr.strip()}
    ok=subprocess.run(["systemctl","is-active","--quiet",service],timeout=10).returncode==0
    update_incident(i,action="restarted "+service,status="RESOLVED" if ok else "VERIFICATION_FAILED",resolved_at=now() if ok else None)
    return {"success":ok,"action":"restarted "+service,"verified":ok}
