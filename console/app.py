1#!/usr/bin/python

from console.file import *
from console.menu import *
from console.cours import *
from console.etudiant import *
from console.note import *

def main():
    all_notes = []
    go_on = True

    Menu.create()
    init_datas()

    while go_on:
        answer = Menu.display()

        if answer == 1:
            File.read()
        elif answer == 2:
            Etudiant.create()
        elif answer == 3:
            Note.create()
        elif answer == 4:
            Etudiant.display_notes()
        elif answer == 5:
            Cours.display_sorted_notes()
        elif answer == 6:
            Cours.delete()
        elif answer == 7:
            File.write()
        elif answer == 8:
            print("A bientôt !")
            go_on = False
        else:
            print("Mauvais choix, veuillez en choisir un autre")

def init_datas():
    e1 = Etudiant("Tony", "Bengué", 26)
    e2 = Etudiant("Thibault", "Magy", 20)

    c1 = Cours("Python", 2020)
    c2 = Cours("PL/SQL", 1995)
    c3 = Cours("PhP", 2018)
    c4 = Cours("Java", 1992)

    e1.add_note(Note(e1, c1, 15))
    e1.add_note(Note(e1, c2, 20))
    e1.add_note(Note(e1, c3, 14))

    e2.add_note(Note(e2, c1, 8))
    #e1.get_notes()

def __main__():
    main()

if __name__ == "__main__":
    __main__()

