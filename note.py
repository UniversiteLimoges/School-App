from cours import Cours, Courses
from etudiant import Etudiant, Etudiants

class Notes(object):
    all_notes = []
    pass

class Note(object):
    # Init a note
    def __init__(self, student, cours, note):
        self.student = student
        self.cours = cours
        self.note = note

        Notes.all_notes.append(self)

    # Display the note added
    def __repr__(self):
        return "La note " + str(self.note) + " est attribuée pour l'étudiant " + self.student.prenom + " " + self.student.nom + "(" + str(self.student.age) + " ans) dans le cours de " + self.cours.nom + " (" + str(self.cours.annee) + ")"

    # Get the note for the current course
    def get_note_course(self):
        print(self.student.prenom + " " + self.student.nom + " (" + str(self.student.age) + " ans) : " + str(self.note))

    # Add a note for a student
    # Cette Fonction permet de créer une note, étant donné qu'une note est liée à un utilisateur et à un cours il faut aussi renvoyer les tableaux d'etudiant et de cours mis à jour
    def create():
        note = input("Note à attribuer : ")
        print("Liste des étudiants : ")

        for index, student in enumerate(Etudiants.all_students):
            print(str(index + 1) + ". " , student)
        answer_student = int(input("Votre choix d'étudiant : "))

        for index, cours in enumerate(Courses.all_courses):
            print(str(index + 1) + ". " , cours)
        answer_course = int(input("Votre choix du cours : "))

        # TODO: Corriger ce code selon le modèle de classe choisi
        new_note = Note(Etudiants.all_students[answer_student - 1], Courses.all_courses[answer_course - 1], note)

        # On ajoute cette instance au bon étudiant du tableau des étudiants et au bon cours des tableaux des cours
        Etudiants.all_students[answer_student - 1].add_note(new_note)
        Courses.all_courses[answer_course - 1].add_note(new_note)
        print(new_note)
