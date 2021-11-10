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
