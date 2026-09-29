from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from app.monitor import collect_metrics,scan_once
from app.storage import init_db,list_incidents
from app.remediation import restart_service
app=FastAPI(title="OpsPilot API",version="1.0.0"); init_db()
DASHBOARD=Path(__file__).resolve().parents[1]/"dashboard"/"index.html"
@app.get("/",response_class=HTMLResponse)
def dashboard(): return DASHBOARD.read_text()
@app.get("/api/health")
def health(): return {"status":"ok"}
@app.get("/api/metrics")
def metrics(): return collect_metrics()
@app.get("/api/incidents")
def incidents(limit:int=50): return list_incidents(max(1,min(limit,200)))
@app.post("/api/scan")
def scan():
    m,f=scan_once(); return {"metrics":m,"findings":f}
@app.post("/api/incidents/{incident_id}/remediate")
def remediate(incident_id:int,service:str="opspilot-demo.service"):
    if not any(x["id"]==incident_id for x in list_incidents(200)): raise HTTPException(404,"Incident not found")
    try:return restart_service(incident_id,service)
    except ValueError as e:raise HTTPException(400,str(e))
