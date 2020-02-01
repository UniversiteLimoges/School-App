class Etudiants(object):
    all_students = []
    pass

# class Etudiant(object, Etudiants):
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
            print(note)
            #print(note.cours.nom + " (" + note.cours.annee + ") : " + note.note)
