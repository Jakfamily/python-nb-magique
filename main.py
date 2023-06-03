import random


def jeu_nombre_magique():

    print("###############################")
    print("# Bienvenue au nombre magique #")
    print("###############################")

    nb_magique = random.randint(1, 50)
    estimation = -1  # initialisation de l'estimation
    tentative = 0  # initialisation de la tentative
    max_tentatives = 5  # initialisation du nombre de tentatives max

    while estimation != nb_magique and tentative < max_tentatives:
        tentatives_restantes = max_tentatives - tentative
        print()
        print("Tentatives restantes : " + str(tentatives_restantes))
        print()
        instruction = input("Quelle est votre estimation ? [Q:Quitter] ")
        if instruction.lower() == 'q':  # lower convertie tout en minuscule
            print()
            print("Merci d'avoir participé ! Le juste prix était : " + str(nb_magique))
            break

        if not instruction.isnumeric():  # isnumeric verifie si la valeur est un nombre
            print()
            print("Veuillez saisir un nombre valide ou la lettre Q pour quitter!")
            print()
            continue

        estimation = int(instruction)
        tentative += 1

        if estimation < nb_magique:
            print()
            print("Trop petit !")
            print()
        elif estimation > nb_magique:
            print()
            print("Trop grand !")
            print()
        else:
            print("Bravo, tu as gagné !")
            break

    if tentative == 10 and estimation != nb_magique:
        print()
        print("Vous avez perdu ! Le juste prix était : " + str(nb_magique))


jeu_nombre_magique()
