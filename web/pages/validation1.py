import cgi
form = cgi.FieldStorage()

# Encoding
import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering = 1)
print("Content-type: text/html; charset=utf-8\n")

from classes.pythonSqlConnect import PythonSqlConnect

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
</body>
"""
print(html)

# Values get from the form
firstName = form.getvalue("firstName")
lastName = form.getvalue("lastName")
age = form.getvalue("age")

try:
    con = PythonSqlConnect()
    con.populateStudent(firstName, lastName, age)

except Exception as e:
    print("Exception occured:{}".format(e))

finally:
    #disconnect from server
    con.closeCon()

    print("<a href='../index.py'>Retour au menu principal</a>")




