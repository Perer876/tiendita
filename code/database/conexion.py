import mysql.connector
from .utilidades import *

def create_connection(user='app_conn', password='superstrongpassword123456', database ='tiendita'):
    try:
        return mysql.connector.connect(
            user = user,
            password = password,
            database = database
        )
    except mysql.connector.Error as e:
        print ("Error connecting to database\n    " + str(e))

def insert(table, **kwargs):
    conn = create_connection()
    if not conn: return False
    cursor = conn.cursor()

    try:
        columns = ",".join(list(kwargs.keys()))
        values = ",".join([f"'{str(value)}'" for value in kwargs.values()])
        query = f"INSERT INTO {str(table)} ({columns}) VALUES ({values});"
        
        cursor.execute(query)
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as e:
        print(f"Error at insert into table <{table}>\n    query = {query}\n" + str(e))
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

def select(table, *args, condition:str=None, **kwargs):
    conn = create_connection()
    if not conn: return False
    cursor = conn.cursor()

    try:
        columns = column_names(args)
        condition = where_condition(condition, kwargs)
        query = f"SELECT {columns} FROM {str(table)} {condition};"
        
        cursor.execute(query)

        query_list = []
        for row in cursor.fetchall():
            item = {}
            if len(args) == 0:
                args = get_column_names(cursor.description)
            for i, column in enumerate(args):
                item[column] = row[i]
            query_list.append(item)

        return query_list
    except mysql.connector.Error as e:
        print(f"Error at select from table <{table}>\n    query = {query}\n" + str(e))
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

def update(table, relations:dict, condition:str=None, **kwargs):
    conn = create_connection()
    if not conn: return False
    cursor = conn.cursor()

    try:
        assignments = assignment_list(relations)
        condition = where_condition(condition, kwargs)
        query = f"UPDATE {str(table)} SET {assignments} {condition};"
        
        cursor.execute(query)
        conn.commit()
        
        if cursor.rowcount > 0:
            return True
        return False
    except mysql.connector.Error as e:
        print(f"Error at update from table <{table}>\n    query = {query}\n" + str(e))
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()

def delete(table, condition:str=None, **kwargs):
    conn = create_connection()
    if not conn: return False
    cursor = conn.cursor()

    try:
        condition = where_condition(condition, kwargs)
        query = f"DELETE FROM {str(table)} {condition};"
        
        cursor.execute(query)
        conn.commit()

        if cursor.rowcount > 0:
            return True
        return False
    except mysql.connector.Error as e:
        print(f"Error at delete from table <{table}>\n    query = {query}\n" + str(e))
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()
