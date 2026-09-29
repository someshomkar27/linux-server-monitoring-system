import socket,time,psutil
from .config import load_config
from .storage import create_incident,init_db
def collect_metrics():
    vm=psutil.virtual_memory(); disk=psutil.disk_usage("/")
    load=psutil.getloadavg()[0] if hasattr(psutil,"getloadavg") else 0
    n=psutil.cpu_count() or 1
    return {"host":socket.gethostname(),"cpu_percent":psutil.cpu_percent(interval=.2),"memory_percent":vm.percent,
            "disk_percent":disk.percent,"load_per_cpu":load/n,"uptime_seconds":int(time.time()-psutil.boot_time()),
            "process_count":len(psutil.pids())}
def detect(m,config=None):
    t=(config or load_config())["thresholds"]; out=[]
    for cat,key in [("CPU","cpu_percent"),("MEMORY","memory_percent"),("DISK","disk_percent"),("LOAD","load_per_cpu")]:
        if m[key]>=t[key]: out.append({"severity":"HIGH","category":cat,"summary":key+" reached %.1f, threshold %.1f"%(m[key],t[key]),
                                       "diagnosis":cat.lower()+" pressure detected from host metrics"})
    return out
def top_processes(limit=5):
    rows=[]
    for p in psutil.process_iter(["pid","name","username","cpu_percent","memory_percent"]):
        try: rows.append(p.info)
        except (psutil.NoSuchProcess,psutil.AccessDenied): pass
    return sorted(rows,key=lambda x:x.get("cpu_percent") or 0,reverse=True)[:limit]
def scan_once():
    init_db(); m=collect_metrics(); findings=detect(m)
    for f in findings: create_incident({"incident_key":m["host"]+"-"+f["category"]+"-"+str(int(time.time())),
        "severity":f["severity"],"host":m["host"],"category":f["category"],"summary":f["summary"],
        "diagnosis":f["diagnosis"],"action":"PENDING","status":"OPEN"})
    return m,findings
if __name__=="__main__": print(scan_once())
