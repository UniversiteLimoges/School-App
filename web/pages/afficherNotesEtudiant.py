import cgi 
form = cgi.FieldStorage()
#print(form.getvalue("name"))

# Encoding
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <title>Afficher les notes d'un étudiant</title>
</head>
<body>
    <form action="/index.py" method="post">
        <p>Liste des étudiants : </p>
        <ul>
            <li></li>
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