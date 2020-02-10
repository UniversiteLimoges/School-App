import cgi 
form = cgi.FieldStorage()
from classes.pythonSqlConnect import PythonSqlConnect

#print(form.getvalue("name"))

# Encoding
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

# Query and Fetch the students
con = PythonSqlConnect()
courses = con.getAllCourses()

html = """<!DOCTYPE html>
<head>
    <title>supprimer un cours et les notes associées</title>
</head>
<body>
    <form action="validation5.py" method="post">
        <p>Liste des cours : </p>
        <ul>
"""
for course in courses:
    html += "<li>{} - {} ({})</li>".format(course[0], course[1], course[2])

html += """
        </ul>
        <label>Votre choix :
            <input type="number" name="courseChoice" value="" placeholder="Quel cours?" />
        </label><br>
        <input type="submit" name="send" value="Valider">
    </form> 
</body>
</html>
"""
print(html)