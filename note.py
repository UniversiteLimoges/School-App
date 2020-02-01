class Note(object):

    # Init a note
    def __init__(self, student, cours, note):
        self.student = student
        self.cours = cours
        self.note = note

    # Display the note added
    def __repr__(self):
        return "La note " + self.note + " est attribuée pour l'étudiant " + self.student.prenom + " " + self.student.nom + "(" + self.student.age + " ans) dans le cours de " + self.cours.nom + " (" + self.cours.annee + ")"

    # Get the note for the 
    def get_note_course(self):
        print(self.student.prenom + " " + self.student.nom + " (" + self.student.age + " ans) : " + self.note)
