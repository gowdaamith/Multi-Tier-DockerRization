import os
import mysql.connnector

def get_connection():
    return mysql.connector.connect(
            host=os.getenv("DB_HOST","localhost"),
            user=os.getenv("DB_USER","root"),
            password=os.getenv("DB_PASSWORD","rootpassword"),
            database=os.getenv("DB_NAME","employee_db)
     )
