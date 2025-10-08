from flask import Flask, request, jsonify
from db import get_db, row_to_dict
from datetime import datetime

app = Flask(__name__)

@app.get("/")
def root():
    return "API Estudiantes activa. Usa /estudiantes"

def now_iso():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate(data, require_all=False):
    if data is None:
        return "JSON inválido", 400
    req = ("nombre","apellido","aprobado","nota")
    if require_all:
        faltan = [k for k in req if k not in data or str(data[k]).strip()==""]
        if faltan:
            return f"Faltan campos: {', '.join(faltan)}", 400
    if "nota" in data:
        try: float(data["nota"])
        except: return "nota debe ser numérica", 400
    if "aprobado" in data and type(data["aprobado"]) is not bool:
        return "aprobado debe ser booleano", 400
    return None, 200

@app.get("/estudiantes")
def list_estudiantes():
    con = get_db()
    rows = con.execute("SELECT * FROM alumnos ORDER BY id").fetchall()
    return jsonify([row_to_dict(r) for r in rows])

@app.get("/estudiantes/<int:sid>")
def get_estudiante(sid):
    con = get_db()
    row = con.execute("SELECT * FROM alumnos WHERE id=?", (sid,)).fetchone()
    if not row:
        return jsonify({"error":"no encontrado"}), 404
    return jsonify(row_to_dict(row))

@app.post("/estudiantes")
def create_estudiante():
    data = request.get_json(silent=True)
    err, code = validate(data, require_all=True)
    if err: return jsonify({"error": err}), code

    con = get_db()
    cur = con.execute(
        "INSERT INTO alumnos(nombre,apellido,aprobado,nota,fecha) VALUES (?,?,?,?,?)",
        (
            data["nombre"].strip(),
            data["apellido"].strip(),
            bool(data["aprobado"]),
            float(data["nota"]),
            data.get("fecha") or now_iso(),
        ),
    )
    con.commit()
    return jsonify({"message":"creado","id":cur.lastrowid}), 201

@app.put("/estudiantes/<int:sid>")
def update_estudiante(sid):
    data = request.get_json(silent=True)
    err, code = validate(data, require_all=False)
    if err: return jsonify({"error": err}), code

    campos, valores = [], []
    for k in ("nombre","apellido","aprobado","nota","fecha"):
        if k in data and data[k] is not None and str(data[k]).strip()!="":
            v = bool(data[k]) if k=="aprobado" else float(data[k]) if k=="nota" else data[k]
            campos.append(f"{k}=?"); valores.append(v)

    if not campos: return jsonify({"error":"nada que actualizar"}), 400

    con = get_db()
    cur = con.execute(f"UPDATE alumnos SET {', '.join(campos)} WHERE id=?", (*valores, sid))
    con.commit()
    if cur.rowcount==0: return jsonify({"error":"no encontrado"}), 404
    return jsonify({"message":"actualizado","id":sid})

@app.delete("/estudiantes/<int:sid>")
def delete_estudiante(sid):
    con = get_db()
    cur = con.execute("DELETE FROM alumnos WHERE id=?", (sid,))
    con.commit()
    if cur.rowcount==0: return jsonify({"error":"no encontrado"}), 404
    return jsonify({"message":"borrado","id":sid})

if __name__ == "__main__":
    app.run(debug=True)
