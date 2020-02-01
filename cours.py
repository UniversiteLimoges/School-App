class Cours(object):
    all_courses = []

    def __init__(self, nom, annee):
        self.nom = nom
        self.annee = annee

        # Add the course in the list
        Cours.all_courses.append(self)

    def __repr__(self):
        return self.nom + " " + "(" + str(self.annee) + ")"

