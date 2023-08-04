# %%
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# %%
conn = sqlite3.connect("data.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS datos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        curso TEXT NOT NULL
    )
""")

conn.commit()
conn.close()


class Datos(BaseModel):
    nombre: str
    edad: int
    curso: str

app = FastAPI()

@app.post("/agregar/")
async def agregar_datos(datos: Datos):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO datos (nombre, edad, curso) VALUES (?, ?, ?)", (datos.nombre, datos.edad, datos.curso))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}

@app.get("/datos/")
async def obtener_todos_datos():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, edad, curso FROM datos")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"nombre": resultado[0], "edad": resultado[1], "curso": resultado[2]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

@app.get("/consultar/{id}/")
async def consultar_datos(id: int):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, edad, curso FROM datos WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"nombre": resultado[0], "edad": resultado[1], "curso": resultado[2]}
    else:
        return {"mensaje": "Datos no encontrados"}

@app.put("/actualizar/{id}/")
async def actualizar_datos(id: int, datos: Datos):
    conn = sqlite3.connect("data.db")
    cursor = conn.execute()
    cursor.execute("UPDATE datos SET nombre=?, edad=?, curso=? WHERE id=?", (datos.nombre, datos.edad, datos.curso, id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}

@app.delete("/eliminar/{id}/")
async def eliminar_datos(id: int):
    conn = sqlite3.connect("data.db")
    cursor = conn.execute()
    cursor.execute("DELETE FROM datos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}
