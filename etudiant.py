class Etudiants(object):
    all_students = []
    pass

class Etudiant(Etudiants, object):
    next_id = 0
    notes = []

    # Init a student
    def __init__(self, prenom, nom, age):
        self.id = Etudiant.next_id
        Etudiant.next_id += 1

        self.prenom = prenom
        self.nom = nom
        self.age = age

        # Add the student in the list
        Etudiants.all_students.append(self)

    # Add a student
    def create():
        prenom = input("Prenom : ")
        nom = input("Nom : ")
        age = input("Age : ")

        print("\nEtudiant ajouté")
        Etudiant(prenom, nom, age)

    # Display a student
    def __repr__(self):
        return self.prenom + " " + self.nom + " (" + str(self.age) + " ans)"

    # Add a note to the student
    def add_note(self, note):
        self.notes.append(note)

    # Get the notes for the student
    def get_notes(self):
        print("Notes de " + self.prenom + " " + self.nom + " (" + str(self.age) + " ans) : ")
        for note in self.notes:
            print(note.cours.nom + " (" + str(note.cours.annee) + ") : " + str(note.note))

    # Show the notes for the student
    def display_notes():
        print("Liste des étudiants")
        for index, student in enumerate(Etudiants.all_students):
            print(str(index + 1) + ". " , student)
        answer = int(input("Votre choix: "))

        curr_student = Etudiants.all_students[answer - 1]
        curr_student.get_notes()

