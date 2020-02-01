class Courses(object):
    all_courses = []
    pass

class Cours(Courses, object):
    note = []
    def __init__(self, nom, annee):
        self.nom = nom
        self.annee = annee
        # Add the course in the list
        Courses.all_courses.append(self)

    def add_note(self, note):
        self.note.append(note)

    def __repr__(self):
        return self.nom + " " + "(" + str(self.annee) + ")"

