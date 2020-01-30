# ------------------------------------ CLASSES --------------------------------------
# Voici les classes, il y en a trois.
# TODO: create and finish the classes
# TODO: refactor into multiple files

# La classe Etudiant modélise un étudiant, celui-ci à des notes (donc dans une liste), un prénom, un nom et un âge
# l'id permet de différencier deux individus qui auraient le même prénom, nom et âge. Il n'est pas vraiment utile dans le cadre de cet exercice mais il est intéressant de le montrer
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
        """
        Fonction d'ajout d'une note à un élève
        :param note:
        :return: None
        """
        self.notes.append(note)

    def get_notes(self):
        """
        fonction d'affichage de chaque note d'un étudiant
        :return: None
        """
        print("Notes de " + self.prenom + " " + self.nom + " (" + self.age + " ans) : ")
        for note in self.notes:
            print(note.cours.nom + " (" + note.cours.annee + ") : " + note.note)

# La classe Cours représente un cours, cette classe a donc un nom ou intitulé et une année
class Cours(object):
    notes = []
    def __init__(self, nom, annee):
        self.nom = nom
        self.annee = annee

    def __repr__(self):
        return self.nom + " " + "(" + self.annee + ")"

# TODO: créer une fonction check_note(self) qui permet de vérifier que la note est un entier entre 0 et 20 ou 100 (à vérifier)
# La classe Note représente une note, elle est associée à un étudiant et un cours, bien sûr cette classe a une variable note elle même qui prend la valeur de la note
class Note(object):
    def __init__(self, student, cours, note):
        self.student = student
        self.cours = cours
        self.note = note

    def __repr__(self):
        return "La note " + self.note + " est attribuee pour l'étudiant " + self.student.prenom + " " + self.student.nom + "(" + self.student.age + " ans) dans le cours de " + self.cours.nom + " (" + self.cours.annee + ")"

    def get_note_course(self):
        """
        Affichage de la note sous un certain format
        :return: None
        """
        print(self.student.prenom + " " + self.student.nom + " (" + self.student.age + " ans) : " + self.note)

# -------------------------------------- MAIN ----------------------------------------
# TODO: create and finish the main function
# TODO: créer des faux étudiants, cours et notes de manière à avoir un jeu d'essais
# Cette fonction est la fonction principale, c'est à dire la fonction qui va executer toute les autres
# Pour cet exercice on commence par initialiser des étudiants, des cours et des notes en tant que données de jeux d'essais
# Ensuite une boucle principale est lancée jusqu'à ce que l'utilisateur entre '8'
# Tout les choix différents exécutent des fonction différentes
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
        else:
            print("Ce n'est pas une option valable !")

# -------------------------------------- FUNCTIONS ----------------------------------------
def print_menu():
    """
    Fonction d'affichage du menu
    :return: None
    """
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
    # On ouvre le fichier et on le parcours puis si possible on ajoute une ligne dans un tableau
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
def create_note(all_students, all_courses):
    note = input("Note a attribuer : ") # valeur de la note
    print("Liste de étudiants")
    # La boucle suivante affiche chaque étudiants pour que l'utilisateur voit ce qu'il peut choisir
    i = 1
    # TODO: Vérifier la valabilité de l'entrée
    for st in all_students:
        print(i + ". " + st.__repr__())
        i += 1
    # La boucle suivante affiche chaque cours pour que l'utilisateur voit ce qu'il peut choisir
    i = 1
    answer_student = input("Votre choix")
    # TODO: Vérifier la valabilité de l'entrée
    for crs in all_courses:
        print(i + ". " + crs.__repr__())
        i += 1
    answer_course = input("Votre choix")
    # TODO: Corriger ce code selon le modèle de classe choisi
    # On crée notre nouvelle instance de Note
    new_note = Note(all_students[answer_student-1], all_courses[answer_course-1], note)
    # On ajoute cette instance au bon étudiant du tableau des étudiants et au bon cours des tableaux des cours
    all_students[answer_student-1].addNote(new_note)
    all_courses[answer_course-1].addNote(new_note)
    return new_note, all_students, all_courses

# ------------------ 4 -------------------
# Quatrième fonction : Afficher les notes d'un étudiant
def display_student_notes(all_students):
    print("Liste de étudiants")
    i = 1
    for st in all_students:
        print(i + ". " + st.__repr__())
        i += 1
    answer = input("Votre choix")
    # TODO: Vérifier la valabilité de l'entrée
    curr_student = all_students[answer-1]
    # La méthode suivante affiche les notes de l'étudiant
    curr_student.getNotes()

# ------------------ 5 -------------------
# Cinquième fonction : Afficher les notes triées d'un cours
def display_sorted_note(all_courses):
    print("Liste des cours")
    # On affiche tout les choix que l'utilisateur peut faire
    i = 1
    for crs in all_courses:
        print(i + ". " + crs.__repr__())
        i += 1
    answer = input("Votre choix : ")
    # TODO: Vérifier la valabilité de l'entrée
    cours = all_courses[answer-1]
    notes = cours.notes.sort() # On tri donc les notes
    for note in notes:
         # Cette fonction permet d'afficher les notes d'un cours
        note.get_note_course()

# ------------------ 6 -------------------
# TODO: Faire les fonctions qui restent à faire

# -------------------------------------- __MAIN__ ----------------------------------------
def __main__():
    main()