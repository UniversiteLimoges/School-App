import pymysql
import cgi

header = """<!DOCTYPE html>
<head>
    <head><meta http-equiv="Content-Type" content="text/html;charset=UTF-8"></head>
    <title>Mon programme</title>
</head>
<body>
"""
print(header)

# Parameters
tony = {"login": "root", "password": "", "database": "" }
default = {"login": "test", "password": "test", "database": "ruches" }

class PythonSqlConnect(object):
    cursor = None

    def __init__(self, param = None):
        # Open database connection
        connection = pymysql.connect('localhost', param["login"], param["password"], param["database"])
        # Open database connection
        # connection = pymysql.connect('localhost', param["login"], param["password"], param["database"])

        # Cursor
        self.cursor = connection.cursor()

    # Get the version of the database
    def version(self):
        self.cursor.execute("SELECT VERSION()")
        version = self.cursor.fetchone()
        print("Database version: {}".format(version[0]))

    # Create a database
    def createDatabase(table):
        self.cursor.execute("DROP TABLE IF EXISTS " + table)
        sqlQuery = "CREATE DATABASE " + table
        self.cursor.execute(sqlQuery)
        print("Database {} crée avec succès".format(table))

    def displayDatabases(self):
        # SQL query string
        sqlQuery = "SHOW DATABASES"
    
        # Execute the sqlQuery
        self.cursor.execute(sqlQuery)
        print("Database {}".format(table))

        #Fetch all the rows
        databaseList = self.cursor.fetchall()
        for database in databaseList:
            print(database)

try:
    con = PythonSqlConnect(tony)
    con.version()
    
    # db_table = "test"
    # connection = pymysql.connect('localhost', "root", "")
    # cursor = connection.cursor()
    # sqlStatement = "CREATE DATABASE TEST"
    # cursor.execute(sqlStatement)

    # con.createDatabase()

    #createDatabase(cursor, table)

 
        
except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    # disconnect from server
    con.close()

