import sqlite3
from datetime import datetime,timezone
from pathlib import Path
from .config import DB_PATH
def connect():
    Path(DB_PATH).parent.mkdir(parents=True,exist_ok=True)
    c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; return c
def init_db():
    with connect() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT, incident_key TEXT NOT NULL,
        severity TEXT NOT NULL, host TEXT NOT NULL, category TEXT NOT NULL,
        summary TEXT NOT NULL, diagnosis TEXT, action TEXT, status TEXT NOT NULL,
        created_at TEXT NOT NULL, resolved_at TEXT)"""); c.commit()
def create_incident(i):
    init_db()
    with connect() as c:
        x=c.execute("""INSERT INTO incidents
        (incident_key,severity,host,category,summary,diagnosis,action,status,created_at)
        VALUES (?,?,?,?,?,?,?,?,?)""",(i["incident_key"],i["severity"],i["host"],i["category"],
        i["summary"],i.get("diagnosis"),i.get("action"),i.get("status","OPEN"),i.get("created_at") or now()))
        c.commit(); return x.lastrowid
def list_incidents(limit=50):
    init_db()
    with connect() as c: return [dict(r) for r in c.execute("SELECT * FROM incidents ORDER BY id DESC LIMIT ?",(limit,))]
def update_incident(i,**fields):
    a={k:v for k,v in fields.items() if k in {"diagnosis","action","status","resolved_at"}}
    if not a:return
    clause=", ".join(k+"=?" for k in a)
    with connect() as c: c.execute("UPDATE incidents SET "+clause+" WHERE id=?",(*a.values(),i)); c.commit()
def now(): return datetime.now(timezone.utc).isoformat()
