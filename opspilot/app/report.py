from .storage import list_incidents
if __name__=="__main__":
    rows=list_incidents()
    if not rows: print("No incidents recorded.")
    for r in rows: print("#%s %s %s %s — %s"%(r["id"],r["severity"],r["category"],r["status"],r["summary"]))
