import pymysql

class PythonSqlConnect(object):
    # Parameters
    emptyDb = {"login": "root", "password": "", "database": None}
    defaultDb = {"login": "test", "password": "test", "database": "test" }
    tonyDb = {"login": "root", "password": "", "database": "test" }
    thibaultDb = {"login": "admin", "password": "", "database": "test" }

    def __init__(self, param):
        if param["database"] is not None:
            # Open database connection
            self.connection = pymysql.connect('localhost', param["login"], param["password"], param["database"])
        else:
            # Open database connection
            self.connection = pymysql.connect('localhost', param["login"], param["password"])

        # Cursor
        self.cursor = self.connection.cursor()

    # Get the version of the database
    def version(self):
        self.cursor.execute("SELECT VERSION()")
        version = self.cursor.fetchone()
        print("Database version: {}".format(version[0]))

    # Create a database
    def createDatabase(self, table):
        self.cursor.execute("DROP DATABASE {}".format(table))
        sqlQuery = "CREATE DATABASE {}".format(table)
        self.cursor.execute(sqlQuery)

        self.closeCon()
        print("Database {} crée avec succès".format(table))

    # Create tables
    def createTables(self):
        self.cursor.execute("DROP TABLE IF EXISTS Notes")
        self.cursor.execute("DROP TABLE IF EXISTS Students")
        self.cursor.execute("DROP TABLE IF EXISTS Courses")
        sql1 = """
            CREATE TABLE Students
            (
                student_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                prenom VARCHAR(100) NOT NULL,
                nom VARCHAR(100) NOT NULL,
                age INT NOT NULL
            );
        """
        sql2 ="""
            CREATE TABLE Courses
            (
                course_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                nom VARCHAR(100) NOT NULL,
                annee INT 
            );
        """
        sql3 = """
            CREATE TABLE Notes
            (
                note_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                note INT NOT NULL,
                student_id INT NOT NULL,
                course_id INT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES Students(student_id),
                FOREIGN KEY (course_id) REFERENCES Courses(course_id)
            );
        """
        self.cursor.execute(sql1)
        print("<p>Tables etudiants crée avec succès</p>")
        self.cursor.execute(sql2)
        print("<p>Tables cours crée avec succès</p>")
        self.cursor.execute(sql3)
        print("<p>Tables notes crée avec succès</p>")

    # Add datas in the table Student
    def populateStudent(self, prenom, nom, age):
        sql = "INSERT INTO Students (prenom, nom, age) VALUES (%s, %s, %s)"
        val = (prenom, nom, age)
        self.cursor.execute(sql, val)
        self.connection.commit()
        print("<p>L'étudiant {} {} ({} ans) a été ajouté</p>".format(prenom, nom, age))
        #print(self.cursor.rowcount, "record inserted.")

    # Add datas in the table Course table
    def populateCourse(self, nom, annee):
        sql = "INSERT INTO Courses (nom, annee) VALUES (%s, %s)"
        val = (nom, annee)
        self.cursor.execute(sql, val)
        self.connection.commit()
        print("<p>Le cours {} {} a été ajouté</p>".format(nom, annee))

    # Show all databases
    def displayDatabases(self):
        # SQL query string
        sqlQuery = "SHOW DATABASES"
    
        # Execute the sqlQuery
        self.cursor.execute(sqlQuery)
        # print("Database {}".format(table))

        for x in self.cursor:
            print(x) 

    # Close de connection
    def closeCon(self):
        self.connection.close()
