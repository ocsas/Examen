import json, os, sqlite3
import os
print("RUN:", os.path.abspath(__file__))
print("CWD:", os.getcwd())

DB = "alumnos.db"
JSON_PATH = "estudiante.json"

def get_db():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con

def init_db(con):
    con.execute("""
    CREATE TABLE IF NOT EXISTS alumnos(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT NOT NULL,
      apellido TEXT NOT NULL,
      aprobado BOOLEAN NOT NULL,
      nota REAL NOT NULL,
      fecha TEXT NOT NULL
    )
    """)
    con.commit()

def load_json(path):
    if not os.path.exists(path): return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    norm = []
    for s in data:
        fecha = s.get("fecha")
        
        if isinstance(fecha, dict) and "$date" in fecha:
            fecha = fecha["$date"].replace("T"," ").replace("Z","")
        norm.append({
            "nombre": s.get("nombre","").strip(),
            "apellido": s.get("apellido","").strip(),
            "aprobado": bool(s.get("aprobado", False)),
            "nota": float(s.get("nota", 0)),
            "fecha": fecha or "2025-01-01 00:00:00",
        })
    return norm

def seed(con, rows):
   
    con.execute("DELETE FROM alumnos")
    con.executemany(
        "INSERT INTO alumnos(nombre,apellido,aprobado,nota,fecha) VALUES (?,?,?,?,?)",
        [(r["nombre"], r["apellido"], r["aprobado"], r["nota"], r["fecha"]) for r in rows]
    )
    con.commit()

if __name__ == "__main__":
    con = get_db()
    init_db(con)
    rows = load_json(JSON_PATH)
    if not rows:

        rows = [
            {'nombre':'Juan','apellido':'Pérez','aprobado':True,'nota':7.5,'fecha':'2024-09-01 00:00:00'},
            {'nombre':'María','apellido':'López','aprobado':False,'nota':4.2,'fecha':'2024-09-02 00:00:00'},
            {'nombre':'Carlos','apellido':'García','aprobado':True,'nota':8.9,'fecha':'2024-09-03 00:00:00'},
            {'nombre':'Lucía','apellido':'Martínez','aprobado':True,'nota':9.1,'fecha':'2024-09-04 00:00:00'},
            {'nombre':'Sofía','apellido':'Fernández','aprobado':False,'nota':5.0,'fecha':'2024-09-05 00:00:00'},
        ]
    seed(con, rows)
    n = con.execute("SELECT COUNT(*) c FROM alumnos").fetchone()["c"]
    print(f"alumnos.db lista. Registros: {n}")
