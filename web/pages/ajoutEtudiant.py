import cgi 
form = cgi.FieldStorage()

# Encoding
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="./validation1.py" method="post">
        <label>Prénom : 
            <input type="text" name="firstName" value="" placeholder="Votre prénom" />
        </label><br>
        <label>Nom :
            <input type="text" name="lastName" value="" placeholder="Votre nom" />
        </label><br>
        <label>Age :
            <input type="number" name="age" value="" placeholder="Votre age" />
        </label><br>

        <input type="submit" name="send" value="Valider">
    </form> 
</body>
</html>
"""
print(html)