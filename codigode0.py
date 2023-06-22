import sqlite3

class BaseDatos:
    def __init__(self):
        self.conexion = sqlite3.connect("codigode0")
        self.cursor = self.conexion.cursor()

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                NombreCN VARCHAR(255)            
            )
            """
        )        
        self.cursor.execute(
            """INSERT INTO Categorias (NombreCN)
            VALUES ('Penal') """
        )
        self.cursor.execute(
            """INSERT INTO Categorias (NombreCN)
            VALUES ('Civil')"""
        )
        self.cursor.execute(
            """INSERT INTO Categorias (NombreCN)
            VALUES ('Comercial')"""
        )
        self.cursor.execute(
            """INSERT INTO Categorias (NombreCN)
            VALUES ('Familia y Sucesiones')"""
        )
        self.cursor.execute(
            """INSERT INTO Categorias (NombreCN)
            VALUES ('Agrario y Ambiental')"""
        )
        self.cursor.execute(
            """INSERT INTO Categorias (NombreCN)
            VALUES ('Minería')"""
        )
        self.cursor.execute(
            """INSERT INTO Categorias (NombreCN)
            VALUES ('Derecho informático')"""
        )

        # INSERT INTO table_listnames (name, address, tele)
        # SELECT * FROM (SELECT 'Rupert', 'Somewhere', '022') AS tmp
        # WHERE NOT EXISTS (
        #     SELECT name FROM table_listnames WHERE name = 'Rupert'
        # ) LIMIT 1; 

        self.conexion.commit()

base_datos = BaseDatos()
#prueba