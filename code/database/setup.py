import mysql.connector
from .conexion import create_connection

def read_file(path:str):
    with open(path, 'r') as file:
        return file.read()

def create_tables():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        for result in cursor.execute(read_file("code/database/sql/tables.sql"), multi=True):
            None

        conn.commit()
        conn.close()
    except mysql.connector.Error as e:
        print ("Error creating tables\n" + str(e))
    finally:
        if conn:
            cursor.close()
            conn.close()