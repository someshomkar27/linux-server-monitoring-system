import socket,time
from .storage import create_incident
from .remediation import restart_service
if __name__=="__main__":
    i=create_incident({"incident_key":"demo-"+str(int(time.time())),"severity":"HIGH","host":socket.gethostname(),
    "category":"SERVICE","summary":"Demo service health check failed","diagnosis":"Simulated inactive application service",
    "action":"PENDING","status":"OPEN"})
    print("Created incident #"+str(i)); print(restart_service(i,"opspilot-demo.service",dry_run=True))
