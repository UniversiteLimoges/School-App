import console.app as con

general_menu = []
general_menu.append("Console Mode")
general_menu.append("Web mode")
general_menu.append("Quitter")

go_on = True
# https://www.journaldev.com/15539/python-mysql-example-tutorial
#https://gist.github.com/bradmontgomery/2219997
#https://pynative.com/python-mysql-database-connection/
#https://docs.python.org/3/library/cgi.html

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
    elif intAnswer == 2:
        go_on = False
        import server
    elif intAnswer == 3:
        go_on = False
        print("Au revoir")
    else:
        print("Mauvais choix, veuillez en choisir un autre")
