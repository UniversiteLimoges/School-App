from cours import  Courses
from etudiant import Etudiants
from note import Notes

class File(object):
    # Lecture des données depuis un fichier par le biais de leur "parsing"
    def read():
        filename = str(input("Entrez le nom du fichier : "))
        state = None
        # Les tableaux suivants récupèrent les étudiants, cours et notes dans des listes
        students = []
        courses = []
        notes = []

        file = open(filename, 'r', encoding="utf-8")
        Lines = file.read().splitlines() 

        # Strips the newline character
        for line in Lines:
            print(line)

        # with open(file) as lines:
        #     for line in lines.readlines():
        #         if line == "#" and state == "":
        #             state = "student"
        #         elif line == "#" and state == "student":
        #             state = "cours"
        #         elif line == "#" and state == "cours":
        #             state = "notes"
        #         elif state == "student":
        #             students.append(line)
        #         elif state == "cours":
        #             courses.append(line)
        #         elif state == "notes":
        #             notes.append(notes)

        # # Affichage
        # display_students(students)
        # display_courses(courses)
        # display_notes(notes)

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

    # # TODO: les fonction suivantes sont les mêmes : on peut les refactor en une seule fonction
    # def display_students(students):
    #     # On affiche le nombre d'étudiants dans le fichier
    #     print(len(students) + " etudiants :")
    #     # On affiche chaque informations les étudiants
    #     for student in students:
    #         print(student)

    # def display_courses(courses):
    #     # On affiche le nombre de cours dans le fichier
    #     print(len(courses) + " cours :")
    #     # On affiche chaque informations les cours
    #     for course in courses:
    #         print(course)

    # def display_notes(notes):
    #     # On affiche le nombre de notes dans le fichier
    #     print(len(notes) + " notes :")
    #     # On affiche chaque informations les notes
    #     for note in notes:
    #         print(note)