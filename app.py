#from os import system
#from menu import Menu
#from subprocess import Popen
#import console.app as con

general_menu = []
general_menu.append("Console Mode")
general_menu.append("Web mode")
general_menu.append("Quitter")

go_on = True
while go_on:
    print("--------------------------------------------------------")
    for index, item in enumerate(general_menu):
        print(str(index + 1) + ". " , item)

    answer = input("Veuillez choisir le type d'application à lancer : ")
    intAnswer = int(answer)
    print(general_menu[intAnswer- 1])
    print("--------------------------------------------------------")

    if intAnswer == 1:
        go_on = False
        con.main()
        #exec(open("console/app.py"))
        #Menu.create()
        #Popen('python ./console/app.py')
        #system("python ./console/app.py")
    elif intAnswer == 2:
        exec(open("web/server.py"))
    elif intAnswer == 3:
        go_on = False
        print("Au revoir")
    else:
        print("Mauvais choix, veuillez en choisir un autre")