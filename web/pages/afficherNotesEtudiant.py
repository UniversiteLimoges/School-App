import cgi 
from classes.pythonSqlConnect import PythonSqlConnect
form = cgi.FieldStorage()
#print(form.getvalue("name"))

# Encoding
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

# Query and Fetch the students
con = PythonSqlConnect()
students = con.getAllStudents()

html = """<!DOCTYPE html>
<head>
    <title>Afficher les notes d'un étudiant</title>
</head>
<body>
    <form action="validation3.py" method="post">
        <p>Liste des étudiants : </p>
        <ul>
"""
for student in students:
    html += "<li>{} {} {}</li>".format(student[0], student[1], student[2], student[3])

html += """
        </ul>
        <label>Votre choix :
            <input type="number" name="etudiantChoice" value="" placeholder="Quel étudiant?" />
        </label><br>
        <input type="submit" name="send" value="Valider">
    </form> 
</body>
</html>
"""
print(html)