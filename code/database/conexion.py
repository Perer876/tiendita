import mysql.connector

def create_connection(user='app_conn', password='superstrongpassword123456', database ='tiendita'):
    try:
        return mysql.connector.connect(
            user = user,
            password = password,
            database = database
        )
    except mysql.connector.Error as e:
        print ("Error connecting to database\n" + str(e))

def insert(table, **kwargs):    
    try:
        conn = create_connection()
        cursor = conn.cursor()

        columns = ",".join(list(kwargs.keys()))
        values = ",".join([str(value) if not type(value) == str else f"'{value}'" for value in kwargs.values()])
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
