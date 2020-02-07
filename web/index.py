import cgi
import sys
import traceback

# encodingUTF8()
# print("Content-Type: text/html")

sys.stderr = sys.stdout

# Encoding solution
def encodingUTF8():
    import sys
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
    print("Content-type: text/html; charset=utf-8\n")

def createLink(file, string):
    new_str = """<a href="{}.py">{}</a>""".format(file, string)
    print(menu + new_str + "<br>")

header = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
"""

menu = ""

try:
    #import cgi.class
    #cgi.debugPage()

    print(header)
    createLink("./pages/initialisationBase", "1. Créer et peupler la base de données")
    createLink("./pages/ajoutEtudiant", "2. Ajouter un étudiant")
    createLink("./pages/ajoutNote", "3. Ajouter une note")
    createLink("./pages/afficherNotesEtudiant", "4. Afficher les notes d'un étudiant")
    createLink("./pages/afficherNotesTrieesCours", "5. Afficher les notes triées d'un cours")
    createLink("/pages/supprimerCours", "6. Supprimer un cours")

except:
    print("<pre>")
    traceback.print_exc()

