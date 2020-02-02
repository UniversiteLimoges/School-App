class Menu(object):
    list_menu = []

    def create():
        Menu.list_menu.append("Lecture des données depuis un fichier")
        Menu.list_menu.append("Ajouter un étudiant")
        Menu.list_menu.append("Ajouter une note")
        Menu.list_menu.append("Afficher les notes d'un étudiant")
        Menu.list_menu.append("Afficher les notes triées d'un cours")
        Menu.list_menu.append("Supprimer un cours")
        Menu.list_menu.append("Sauvegarder des données dans un fichier")
        Menu.list_menu.append("Quitter")

    def display():
        print("--------------------------------------------------------")
        for index, item in enumerate(Menu.list_menu):
            print(str(index + 1) + ". " , item)

        answer = int(input("Votre choix : "))
        print(Menu.list_menu[answer - 1])
        print("--------------------------------------------------------")

        return answer
