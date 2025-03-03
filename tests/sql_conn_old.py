#load dependencies
import pyodbc

# Using SQL Server Auth
print("For the Live SQL Server Authentication, please enter your")
uid = input("Username: ")
pwd = input("Password: ")

connection = pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=;'
                            'DATABASE=;'
                            'UID=' + uid + ';'
                            'PWD=' + pwd + ';'
                           )