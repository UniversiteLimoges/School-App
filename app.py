# ------------------------------------ CLASSES --------------------------------------
# TODO: create and finish the classes
# TODO: refactor into multiple files
class Etudiant(object):
    next_id = 0
    notes = []
    def __init__(self, prenom, nom, age):
        self.id = Etudiant.next_id
        Etudiant.next_id += 1
        self.prenom = prenom
        self.nom = nom
        self.age = age

    def __repr__(self):
        return self.prenom + " " + self.nom + " (" + self.age + " ans)"

    def add_note(self, note):
        self.notes.append(note)

    def get_notes(self):
        print("Notes de " + self.prenom + " " + self.nom + " (" + self.age + " ans) : ")
        for note in self.notes:
            print(note.cours.nom + " (" + note.cours.annee + ") : " + note.note)

class Cours(object):
    notes = []
    def __init__(self, nom, annee):
        self.nom = nom
        self.annee = annee

    def __repr__(self):
        return self.nom + " " + "(" + self.annee + ")"

class Note(object):
    def __init__(self, student, cours, note):
        self.student = student
        self.cours = cours
        self.note = note

    def __repr__(self):
        return "La note " + self.note + " est attribuee pour l'étudiant " + self.student.prenom + " " + self.student.nom + "(" + self.student.age + " ans) dans le cours de " + self.cours.nom + " (" + self.cours.annee + ")"

    def get_note_course(self):
        print(self.student.prenom + " " + self.student.nom + " (" + self.student.age + " ans) : " + self.note)

# -------------------------------------- MAIN ----------------------------------------
# TODO: create and finish the main function
def main():
    all_students = []
    all_courses = []
    all_notes = []
    go_on = True
    while go_on:
        answer = input("Votre choix : ")
        if answer == 1:
            read_file()
        elif answer == 2:
            student = create_student()
            all_students.append(student)
        elif answer == 3:
            note, all_students, all_courses = create_note(all_students, all_courses)
            all_notes.append(note)
        elif answer == 4:
            pass
        elif answer == 5:
            pass
        elif answer == 6:
            pass
        elif answer == 7:
            pass
        elif answer == 8:
            go_on = False

# -------------------------------------- FUNCTIONS ----------------------------------------
def print_menu():
    print("--------------------------------------------------------")
    print("1 - Lecture des donnees depuis un fichier")
    print("2 - Ajouter un etudiant")
    print("3 - Ajouter une note")
    print("4 - Afficher les notes d'un etudiant")
    print("5 - Afficher les notes triees d'un cours")
    print("6 - Supprimer un cours")
    print("7 - Sauvegarder des donnees dans un fichier")
    print("8 - Quitter")
    print("\n")

# ------------------ 1 -------------------
def read_file():
    file = input("Entrez le nom du fichier : ")
    state = ""
    students = []
    courses = []
    notes = []
    with open(file) as lines:
        for line in lines.readlines():
            if line == "#" and state == "":
                state = "student"
            elif line == "#" and state == "student":
                state = "cours"
            elif line == "#" and state == "cours":
                state = "notes"
            elif state == "student":
                students.append(line)
            elif state == "cours":
                courses.append(line)
            elif state == "notes":
                notes.append(notes)
    display_students(students)
    display_courses(courses)
    display_notes(notes)

# TODO: recuperer les infos avec les fonctions __repr__
def display_students(students):
    print(len(students) + " etudiants :")
    for student in students:
        print(student)

def display_courses(courses):
    print(len(courses) + " cours :")
    for course in courses:
        print(course)

def display_notes(notes):
    print(len(notes) + " notes :")
    for note in notes:
        print(note)

# ------------------ 2 -------------------
def create_student():
    prenom = input("Prenom : ")
    nom = input("Nom : ")
    age = input("Age : ")
    return Etudiant(prenom, nom, age)

# ------------------ 3 -------------------
def create_note(all_students, all_courses):
    note = input("Note a attribuer : ")
    print("Liste de étudiants")
    i = 1
    for st in all_students:
        print(i + ". " + st.__repr__())
        i += 1
    i = 1
    answer_student = input("Votre choix")
    for crs in all_courses:
        print(i + ". " + crs.__repr__())
        i += 1
    answer_course = input("Votre choix")
    # TODO: Corriger ce code selon le modèle de classe choisi
    new_note = Note(all_students[answer_student-1], all_courses[answer_course-1], note)
    all_students[answer_student-1].addNote(new_note)
    all_courses[answer_course-1].addNote(new_note)
    return new_note, all_students, all_courses

# ------------------ 4 -------------------
def display_student_notes(all_students):
    print("Liste de étudiants")
    i = 1
    for st in all_students:
        print(i + ". " + st.__repr__())
        i += 1
    answer = input("Votre choix")
    curr_student = all_students[answer-1]
    curr_student.getNotes()

# ------------------ 5 -------------------
def display_sorted_note(all_courses):
    print("Liste des cours")
    i = 1
    for crs in all_courses:
        print(i + ". " + crs.__repr__())
        i += 1
    answer = input("Votre choix : ")
    cours = all_courses[answer-1]
    notes = cours.notes.sort()
    for note in notes:
        note.get_note_course()



# -------------------------------------- __MAIN__ ----------------------------------------
def __main__():
    main()