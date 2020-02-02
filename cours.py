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

    def __repr__(self):
        return self.nom + " " + "(" + str(self.annee) + ")"

    # Add a note to the current course
    def add_note(self, note):
        self.note.append(note)

    # Delete a course with its notes
    def delete():
        for index, cours in enumerate(Courses.all_courses):
            print(str(index + 1) + ". " , cours)
        answer = int(input("Votre choix: "))

        # Delete the current course
        current_course = Courses.all_courses[answer - 1]
        del(Courses.all_courses[answer - 1])

        # Delete the courses and notes for the current learner
        # for cours in Courses.all_courses:
        #     for student in Etudiants.all_students:
        #         print(student.nom)
        #         print(cours.nom)

        print("Le cours " + current_course.nom + " (" + str(current_course.annee) + ") et les notes associées ont eté supprimées.")

    # Display notes sorted from a course
    def display_sorted_notes():
        print("Liste des cours")
        for index, cours in enumerate(Courses.all_courses):
            print(str(index + 1) + ". " , cours)

        answer = int(input("Votre choix : "))

        # TODO: Vérifier la valabilité de l'entrée
        current_cours = Courses.all_courses[answer - 1]
        #print(current_cours)

        print(current_cours[0])
        notes = current_cours.notes.sort() # On tri donc les notes

        for note in notes:
            # Cette fonction permet d'afficher les notes d'un cours
            note.get_note_course()
