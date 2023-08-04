import csv

def leer_datos_csv(archivo_csv):
    datos = []
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            datos.append(fila)
    return datos

import sqlite3

def crear_tabla():
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos_scraping (
            Título TEXT,
            SKU TEXT,
            Original TEXT,
            Descuento TEXT,
            Envío TEXT,
            Stock TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def insertar_datos(datos):
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()
    for fila in datos:
        cursor.execute('INSERT INTO datos_scraping (Título, SKU, Original, Descuento, Envío, Stock) VALUES (?, ?, ?)', 
                       (fila['Título'], fila['SKU'], fila['Precio Original'], fila['Precio Descuento'], fila['Precio Envío'], fila['Stock']))
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    archivo_csv = "dataset/web scraping/Promociones-Cyberpuerta-01-08-2023.csv"
    datos = leer_datos_csv(archivo_csv)
    crear_tabla()
    insertar_datos(datos)
    print("Base de datos creada exitosamente con los datos del archivo CSV")