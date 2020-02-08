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
thibault = {"login": "admin", "password": "", "database": "test" }
default = {"login": "test", "password": "test", "database": "ruches" }

class PythonSqlConnect(object):

    def __init__(self, param = None):
        # Open database connection
        self.connection = pymysql.connect('localhost', param["login"], param["password"], param["database"])
        # Open database connection
        # connection = pymysql.connect('localhost', param["login"], param["password"], param["database"])

        # Cursor
        self.cursor = self.connection.cursor()

    # Get the version of the database
    def version(self):
        self.cursor.execute("SELECT VERSION()")
        version = self.cursor.fetchone()
        print("Database version: {}".format(version[0]))

    # Create a database
    def createDatabase(self, table):
        self.cursor.execute("DROP TABLE IF EXISTS " + table)
        sqlQuery = "CREATE DATABASE " + table
        self.cursor.execute(sqlQuery)
        print("Database {} crée avec succès".format(table))

    def createTables(self):
        self.cursor.execute("DROP TABLE IF EXISTS Notes")
        self.cursor.execute("DROP TABLE IF EXISTS Students")
        self.cursor.execute("DROP TABLE IF EXISTS Courses")
        sql1 = """
            CREATE TABLE Students
            (
               	student_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                prenom VARCHAR(100),
                nom VARCHAR(100),
                age INT
            );
        """
        sql2 ="""
            CREATE TABLE Courses
            (
                course_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                nom VARCHAR(100),
                annee INT
            );
        """
        sql3 = """
            CREATE TABLE Notes
           (
               note_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
               note INT,
               student_id INT,
               course_id INT,
               FOREIGN KEY (student_id) REFERENCES Students(student_id),
               FOREIGN KEY (course_id) REFERENCES Courses(course_id)
           );
        """
        self.cursor.execute(sql1)
        self.cursor.execute(sql2)
        self.cursor.execute(sql3)
        print("Tables créées")

    def populateStudent(self, prenom, nom, age):
        sql = """
            INSERT INTO Student (prenom, nom, age)
            VALUES
            ( '""" + prenom + """', '""" + nom + """', '""" + age + """');
        """
        self.cursor.execute(sql)

    def populateCourse(self, nom, annee):
        sql = """
            INSERT INTO Student (nom, annee)
            VALUES
            ('""" + nom + """', '""" + annee + """');
        """
        self.cursor.execute(sql)
    

    def displayDatabases(self, table):
        # SQL query string
        sqlQuery = "SHOW DATABASES"
    
        # Execute the sqlQuery
        self.cursor.execute(sqlQuery)
        print("Database {}".format(table))

        #Fetch all the rows
        databaseList = self.cursor.fetchall()
        for database in databaseList:
            print(database)

    def closeCon(self):
        self.connection.close()

try:
    con = PythonSqlConnect(thibault)
    con.version()
    # con.createDatabase('test')
    con.createTables()
    con.displayDatabases('test')
    con.closeCon()

    
    # db_table = "test"
    # connection = pymysql.connect('localhost', "root", "")
    # with con.cursor() as cursor:
    #     sql = "CREATE DATABASE TEST"
    #     cursor.execute(sql)


except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    # disconnect from server
    print("DONE")

