from cours import Cours, Courses
from etudiant import Etudiant, Etudiants
from note import Note

# -------------------------------------- MAIN ----------------------------------------
# TODO: create and finish the main function
menu = []

def main():
    all_notes = []
    go_on = True

    toto1 = Etudiant("Tony", "Bengué", 24)
    toto2 = Etudiant("Jean", "Gui", 30)

    cours1 = Cours("Python", 2020)
    cours2 = Cours("PL/SQL", 1995)

    toto1.add_note(Note(toto1, cours1, 15))
    toto1.add_note(Note(toto1, cours1, 20))
    toto1.add_note(Note(toto1, cours2, 17))
    toto1.add_note(Note(toto1, cours2, 18))
    toto1.get_notes()
    print(toto1)

    create_menu()

    while go_on:
        answer = print_menu()

        if answer == 1:
            read_file()
        elif answer == 2:
            student = create_student()
            Etudiants.all_students.append(student)
        elif answer == 3:
            create_note()

            #note, all_students, all_courses = create_note(Etudiant.all_students, all_courses)
            #all_notes.append(note)
        elif answer == 4:
            display_student_notes()
        elif answer == 5:
            display_sorted_note()
        elif answer == 6:
            delete_course()
        elif answer == 7:
            pass
        elif answer == 8:
            go_on = False
        else:
            print("Mauvais choix, veuillez en choisir un autre")

# -------------------------------------- FUNCTIONS ----------------------------------------
def create_menu():
    print("--------------------------------------------------------")
    menu.append("Lecture des données depuis un fichier")
    menu.append("Ajouter un étudiant")
    menu.append("Ajouter une note")
    menu.append("Afficher les notes d'un étudiant")
    menu.append("Afficher les notes triées d'un cours")
    menu.append("Supprimer un cours")
    menu.append("Sauvegarder des données dans un fichier")
    menu.append("Quitter")

def print_menu():
    print("--------------------------------------------------------")
    for index, item in enumerate(menu):
        print(str(index + 1) + ". " , item)

    answer = int(input("Votre choix : "))
    print(menu[answer - 1])
    print("--------------------------------------------------------")

    return answer

# ------------------ 1 -------------------
# Première fonction : Lecture des données depuis un fichier
#Les fichiers sont lus par le biais de leur "parsing"
def read_file():
    # On demande le nom du fichier à l'utilisateur
    # TODO: Vérifier si l'entrée est valable
    file = input("Entrez le nom du fichier : ")
    state = "" # Cette variable permet d'établir si la lecture en est aux étudiants, aux cours ou aux notes
    # Les tableaux suivants récupèrent les étudiants, cours et notes dans des listes
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
    # Pour chaque tableaux on les affiches via les fonctions qui suivent
    display_students(students)
    display_courses(courses)
    display_notes(notes)

# TODO: les fonction suivantes sont les mêmes : on peut les refactor en une seule fonction
def display_students(students):
    # On affiche le nombre d'étudiants dans le fichier
    print(len(students) + " etudiants :")
    # On affiche chaque informations les étudiants
    for student in students:
        print(student)

def display_courses(courses):
    # On affiche le nombre de cours dans le fichier
    print(len(courses) + " cours :")
    # On affiche chaque informations les cours
    for course in courses:
        print(course)

def display_notes(notes):
    # On affiche le nombre de notes dans le fichier
    print(len(notes) + " notes :")
    # On affiche chaque informations les notes
    for note in notes:
        print(note)

# ------------------ 2 -------------------
# Deuxième fonction : Ajouter un etudiant
# La fonction suivante permet de créer un utilisateur selon ses entrée (prenom,nom,age)
def create_student():
    prenom = input("Prenom : ")
    nom = input("Nom : ")
    age = input("Age : ")

    return Etudiant(prenom, nom, age)

# ------------------ 3 -------------------
# Troisième fonction : Ajouter une note
# Cette Fonction permet de créer une note, étant donné qu'une note est liée à un utilisateur et à un cours il faut aussi renvoyer les tableaux d'etudiant et de cours mis à jour
def create_note():
    note = input("Note à attribuer : ")
    print("Liste des étudiants : ")

    for index, student in enumerate(Etudiants.all_students):
        print(str(index + 1) + ". " , student)
    answer_student = int(input("Votre choix d'étudiant : "))

    for index, cours in enumerate(Courses.all_courses):
        print(str(index + 1) + ". " , cours)
    answer_course = int(input("Votre choix du cours : "))

    # TODO: Corriger ce code selon le modèle de classe choisi
    #print()
    new_note = Note(Etudiants.all_students[answer_student-1], Courses.all_courses[answer_course-1], note)
    # On ajoute cette instance au bon étudiant du tableau des étudiants et au bon cours des tableaux des cours
    Etudiants.all_students[answer_student-1].add_note(new_note)
    Courses.all_courses[answer_course-1].add_note(new_note)
    print(new_note)
    # new_note.__repr__()

# ------------------ 4 -------------------
# Quatrième fonction : Afficher les notes d'un étudiant
def display_student_notes():
    print("Liste des étudiants")
    for index, st in enumerate(Etudiants.all_students):
        print(str(index + 1) + ". " , st)
    answer = int(input("Votre choix: "))
    # TODO: Vérifier la valabilité de l'entrée
    curr_student = Etudiants.all_students[answer-1]
    # La méthode suivante affiche les notes de l'étudiant
    curr_student.get_notes()

# ------------------ 5 -------------------
# Cinquième fonction : Afficher les notes triées d'un cours
def display_sorted_note():
    print("Liste des cours")
    # On affiche tout les choix que l'utilisateur peut faire
    i = 1
    for crs in Courses.all_courses:
        print(i + ". " + crs.__repr__())
        i += 1
    answer = input("Votre choix : ")
    # TODO: Vérifier la valabilité de l'entrée
    cours = Courses.all_courses[answer-1]
    notes = cours.notes.sort() # On tri donc les notes
    for note in notes:
         # Cette fonction permet d'afficher les notes d'un cours
        note.get_note_course()

# ------------------ 6 -------------------
def delete_course():
    for index, cours in enumerate(Courses.all_courses):
        print(str(index + 1) + ". " , cours)
    answer = int(input("Votre choix: "))
    to_delete = Courses.all_courses[answer-1]
    del(Courses.all_courses[answer-1])
    print("Le cours " + to_delete.name + " (" + int(to_delete.annee) + ") et les notes associees ont ete supprimees.")

# -------------------------------------- __MAIN__ ----------------------------------------
def __main__():
    main()

if __name__ == "__main__":
    __main__()

