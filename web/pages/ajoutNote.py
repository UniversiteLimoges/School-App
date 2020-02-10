import cgi
from classes.pythonSqlConnect import PythonSqlConnect
form = cgi.FieldStorage()
#print(form.getvalue("name"))

# Encoding
import sys

# Query and Fetch the students
con = PythonSqlConnect()
students = con.getAllStudents()
courses = con.getAllCourses()

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="validation2.py" method="post">
        <label>Note à attribuer :
            <input type="number" name="note" value="" placeholder="Note" />
        </label><br>
        <p>Liste des étudiants : </p>
        <ul>
"""

for student in students:
    html += "<li>{} - {} {} {}</li>".format(student[0], student[1], student[2], student[3])

html += """
        </ul>
        <label>Votre choix :
            <input type="number" name="etudiantChoice" value="" placeholder="A quel étudiant?" />
        </label><br>
        <p>Liste des cours : </p>
        <ul>
"""

for course in courses:
    html += "<li>{} {}</li>".format(course[0], course[1], course[2])

html += """
        </ul>
        <label>Votre choix :
            <input type="number" name="courseChoice" value="" placeholder="A quel cours?" />
        </label><br>
        <input type="submit" name="send" value="Valider">
    </form>
</body>
</html>
"""
print(html)
