import cgi 
form = cgi.FieldStorage()
#print(form.getvalue("name"))

# Encoding
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/index.py" method="post">
        <label>Note à attribuer : 
            <input type="number" name="note" value="" placeholder="Note" />
        </label><br>
        <p>Liste des étudiants : </p>
        <ul>
            <li></li>
        </ul>
        <label>Votre choix :
            <input type="number" name="etudiantChoice" value="" placeholder="A quel étudiant?" />
        </label><br>
        <p>Liste des cours : </p>
        <ul>
            <li></li>
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