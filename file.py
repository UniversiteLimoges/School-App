from cours import  Courses
from etudiant import Etudiants
from note import Notes

class File(object):
    # Lecture des données depuis un fichier par le biais de leur "parsing"
    def read():
        filename = str(input("Entrez le nom du fichier : "))

        try:
            file = open(filename, 'r', encoding="utf-8")
            Lines = file.read().splitlines()
            file.close()

            # Strips the newline character
            for line in Lines:
                print(line)
        except IOError:
            print("Impossible de trouver ce fichier")


    def stringsForWrite(file, table, string):
        file.write(str(len(table)) + " " + string + ": \n")
        for i in table:
            file.write(str(i) + "\n")

    # Write students, courses and notes in a file
    def write():
        filename = str(input("Entrez le nom du fichier : "))
        file = open(filename,"w+", encoding="utf-8")

        File.stringsForWrite(file, Etudiants.all_students, "étudiants")
        File.stringsForWrite(file, Courses.all_courses, "cours")
        File.stringsForWrite(file, Notes.all_notes, "notes")

        print("Les données ont été sauvegardées")
        file.close()
