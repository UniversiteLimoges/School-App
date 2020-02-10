import pymysql

class PythonSqlConnect(object):
    # To modify
    databaseName = "tonybengue"
    dbLogin = "root"
    dbPassword = ""

    # To create the database
    emptyDb = {"login": "root", "password": "", "database": None}

    def __init__(self, param = None):
        # To initialize the connection
        if param is None:
            self.connection = pymysql.connect('localhost', PythonSqlConnect.dbLogin, PythonSqlConnect.dbPassword, PythonSqlConnect.databaseName)
        elif param["database"] is None:
            self.connection = pymysql.connect('localhost', param["login"], param["password"])

        # Cursor
        self.cursor = self.connection.cursor()
    
    # Get the version of the database
    def version(self):
        self.cursor.execute("SELECT VERSION()")
        version = self.cursor.fetchone()
        print("<p>Database version: {}</p>".format(version[0]))

    # Create a database
    def createDatabase(self, table):
        self.cursor.execute("DROP DATABASE IF EXISTS {}".format(table))
        sqlQuery = "CREATE DATABASE {}".format(table)
        self.cursor.execute(sqlQuery)

        self.closeCon()
        print("<p>Database {} crée avec succès</p>".format(table))

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
                course_id INT NOT NULL
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

    # Add note for the current user
    def addNote(self, st_prenom, st_nom, course, note):
        sql1 = "SELECT student_id FROM students WHERE prenom='{}' AND nom='{}'".format(st_prenom, st_nom)
        self.cursor.execute(sql1)
        student_id = self.cursor.fetchone()

        sql2 = "SELECT course_id FROM courses WHERE nom='{}'".format(course)
        self.cursor.execute(sql2)
        course_id = self.cursor.fetchone()

        ressql = "INSERT INTO notes (note, student_id, course_id) VALUES ({}, {}, {})".format(int(note), student_id[0], course_id[0])
        self.cursor.execute(ressql)
        self.connection.commit()
        print("<p>La note {} pour le cours de {} a été ajoutée pour {} {}</p>".format(note, course, st_prenom, st_nom))

    # Add a note by the student id and the course id
    def addNoteById(self, note, student_id, course_id):
        sql = "INSERT INTO notes (note, student_id, course_id) VALUES ({}, {}, {})".format(note, student_id, course_id)
        self.cursor.execute(sql)
        self.connection.commit()
        print("<p>La note {} pour le cours {} a été ajoutée pour l'étudiant {}</p>".format(note, course_id, student_id))

    # Display all notes for the current student
    def displayNotesForStudent(self, student_id):
        student = self.getStudentById(student_id)
        print("<p>Notes de {} {} ({} ans) : </p>".format(student[1], student[2], student[3]))

        notes = self.getNotesByStudentId(student[0])

        print("<ul>")
        for note in notes:
            # print(note)
            courses = self.getCourseById(note[3])
            print("<li> {} ({}) : {}</li>".format(courses[1], courses[2], note[1]))
        print("</ul>")

    # Delete a course by id
    def deleteCourse(self, course_id):
        sql = "DELETE FROM courses WHERE course_id= {}".format(course_id)
        self.cursor.execute(sql)
        self.connection.commit()
        print("<p>Le cours {} et les notes associées ont été supprimées</p>".format(course_id))

    # Get all students
    def getAllStudents(self):
        sql = "SELECT * FROM students"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()

        return res

    # Get all courses
    def getAllCourses(self):
        sql = "SELECT * FROM courses"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()

        return res

    # Get the student by the id
    def getStudentById(self, student_id):
        sql1 = "SELECT * FROM students WHERE student_id={}".format(student_id)
        self.cursor.execute(sql1)
        student = self.cursor.fetchone()

        return student

    # Get the course by the id
    def getCourseById(self, course_id):
        # Get the student by the id
        sql1 = "SELECT * FROM courses WHERE course_id={}".format(course_id)
        self.cursor.execute(sql1)
        student = self.cursor.fetchone()

        return student

    # Get all notes by the student_id
    def getNotesByStudentId(self, student_id):
        sql = "SELECT * FROM notes WHERE student_id={}".format(student_id)
        self.cursor.execute(sql)
        notes = self.cursor.fetchall()

        return notes

    # Show all databases
    def displayDatabases(self):
        # SQL query string
        sqlQuery = "SHOW DATABASES"

        # Execute the sqlQuery
        self.cursor.execute(sqlQuery)
        # print("Database {}".format(table))

        for x in self.cursor:
            print(x)

    # Close the connection
    def closeCon(self):
        self.connection.close()
