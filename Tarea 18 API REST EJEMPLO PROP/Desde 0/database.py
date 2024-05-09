import sqlite3

def crear_conexion():
    conn = sqlite3.connect('calculadora.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS historial_compuesto
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operacion TEXT,
                    num1 REAL,
                    num2 REAL,
                    resultado REAL)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS historial_unico
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    operacion TEXT,
                    num3 REAL,
                    resultado REAL)''')
    return conn

def guardar_operacion_compuesta(operacion, num1, num2, resultado):
    conn = crear_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO historial_compuesto (operacion, num1, num2, resultado) VALUES (?, ?, ?, ?)",
                   (operacion, num1, num2, resultado))
    conn.commit()
    conn.close()

def guardar_operacion_unica(operacion, num3, resultado):
    conn = crear_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO historial_unico (operacion, num3, resultado) VALUES (?, ?, ?)",
                   (operacion, num3, resultado))
    conn.commit()
    conn.close()
 
def obtener_historial_compuesto():
    conn = crear_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historial_compuesto")
    historial = cursor.fetchall()
    conn.close()
    return historial

def obtener_historial_unico():
    conn = crear_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historial_unico")
    historial = cursor.fetchall()
    conn.close()
    return historial