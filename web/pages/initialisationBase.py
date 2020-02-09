import cgi

# Encoding
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

# From folder classes in the module pythonSqlConnect import the Class PythonSqlConnect
from classes.pythonSqlConnect import PythonSqlConnect

header = """<!DOCTYPE html>
<head>
    <head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head>
    <title>Mon programme</title>
</head>
<body>
"""
print(header)

try:
    # Create Database
    con = PythonSqlConnect(PythonSqlConnect.emptyDb)
    con.createDatabase('test')

    # Create tables
    con = PythonSqlConnect(PythonSqlConnect.tonyDb)
    con.createTables()

    # Populate the tables
    con.populateStudent("Marc", "Zuckerberg", 34)
    con.populateStudent("Bill", "Gates", 63)
    con.populateCourse("Deep Learning", 2018)
    con.populateCourse("Python", 2010)

    # con.version()
    # con.displayDatabases()

except Exception as e:
    print("Exception occured:{}".format(e))

finally:
    # disconnect from server
    con.closeCon()
    print("<a href='../index.py'>Retour au menu principal</a>")
