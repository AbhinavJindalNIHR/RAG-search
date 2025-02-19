#load dependencies
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch credentials securely
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
uid = os.getenv("DB_USER")
pwd = os.getenv("DB_PASSWORD")

# # Using SQL Server Auth
# print("For the Live SQL Server Authentication, please enter your")
# uid = input("Username: ")
# pwd = input("Password: ")

try:
    connection = pyodbc.connect(
        f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'
    )
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")


# connection = pyodbc.connect('DRIVER={SQL Server};'
#                             'SERVER=;'
#                             'DATABASE=;'
#                             'UID=' + uid + ';'
#                             'PWD=' + pwd + ';'
#                            )