import random
def combat():
    difficulté = str(input("Choisissez la difficulté : facile ou difficile ")).lower()
    if difficulté == "facile":
        pv_joueur = random.randint(14,20)
        pv_monstre = random.randint(20,28)
        max_potions = 3
        dégats_joueur = 0
        dégats_monstre = 0
        défense_joueur = 0
        soins_potion = 0
        attaque_critique_joueur = 0
        attaque_critique_monstre = 0
        mod_easy = 1

        while pv_joueur > 0 and pv_monstre > 0 :
            print ("Vous avez", pv_joueur ,"PV")
            print ("Le monstre a", pv_monstre ,"PV")
            choix = str(input("Que voulez-vous faire ? attaquer, se défendre ou potion ")).lower()

            if choix == "mode easy" :
                if mod_easy > 0:
                    pv_joueur += 100
                    mod_easy -= 1
                else:
                    print("Mode déjà activé")

            elif choix == "attaquer" :
                dégats_joueur = random.randint (2,11)
                dégats_monstre = random.randint (1,10)
                attaque_critique_joueur = random.randint (1,10)
                attaque_critique_monstre = random.randint (1,10)

                if attaque_critique_joueur == 5 :
                    dégats_joueur *= 2
                elif attaque_critique_monstre == 5 :
                    dégats_monstre *= 2
                else:
                    pass

                if dégats_monstre > dégats_joueur :
                    pv_joueur -= (dégats_monstre - dégats_joueur)
                    print ("Vous avez subit", dégats_monstre - dégats_joueur ,"dégat(s)")

                elif dégats_joueur > dégats_monstre :
                    pv_monstre -= (dégats_joueur - dégats_monstre)
                    print ("Vous avez infligé", dégats_joueur - dégats_monstre ,"dégat(s) au monstre" )

                else :
                    print ("Égalité, personne ne subit de dégats")

            elif choix == "se défendre" :
                défense_joueur = random.randint (1,9)
                dégats_monstre = random.randint (1,5)

                if dégats_monstre > défense_joueur :
                    pv_joueur -= (dégats_monstre - défense_joueur)
                    print ("Vous avez subit", dégats_monstre - défense_joueur ,"dégat(s)")

                else :
                    pv_joueur += (défense_joueur - dégats_monstre)
                    print ("Vous avez récupéré", défense_joueur - dégats_monstre ,"PV")

            elif choix == "potion" :

                if max_potions > 0 :
                    soins_potion = random.randint (-2,10)
                    pv_joueur += soins_potion
                    max_potions -= 1

                    if soins_potion >= 0:
                        print ("Vous avez récupéré", soins_potion, "PV")

                    else :
                        print ("Vous vous êtes empoisonnés : vous perdez", soins_potion, "PV")
                else:
                    print ("Vous n'avez plus de potions")

            elif choix == "coup de ceinture":
                print ("Vous avez infligé", pv_monstre ,"dégat(s) au monstre" )
                pv_monstre = 0

            else:
                print("Vous ne pouvez pas faire ça")

        if pv_joueur <= 0 :
            print ("Vous avez perdu, le monstre a gagné")

        elif pv_monstre <= 0 :
            print ("Vous avez gagné, le monstre a perdu")

        else:
            pass

    elif difficulté == "difficile":
        pv_joueur = random.randint(10,20)
        pv_monstre = random.randint(22,32)
        max_potions = 1
        dégats_joueur = 0
        dégats_monstre = 0
        défense_joueur = 0
        soins_potion = 0
        attaque_critique_joueur = 0
        attaque_critique_monstre = 0
        mod_easy = 1

        while pv_joueur > 0 and pv_monstre > 0 :
            print ("Vous avez", pv_joueur ,"PV")
            print ("Le monstre a", pv_monstre ,"PV")
            choix = str(input("Que voulez-vous faire ? attaquer, se défendre ou potion ")).lower()

            if choix == "mode easy" :
                if mod_easy > 0:
                    pv_joueur += 100
                    mod_easy -= 1
                else:
                    print("Mode déjà activé")

            if choix == "attaquer" :
                dégats_joueur = int(random.randint (1,10))
                dégats_monstre = int(random.randint (1,15))
                attaque_critique_joueur = random.randint (1,10)
                attaque_critique_monstre = random.randint (1,10)

                if attaque_critique_joueur == 5 :
                    dégats_joueur *= 2
                elif attaque_critique_monstre == 5 :
                    dégats_monstre *= 2
                else:
                    pass

                if dégats_monstre > dégats_joueur :
                    pv_joueur -= (dégats_monstre - dégats_joueur)
                    print ("Vous avez subit", dégats_monstre - dégats_joueur ,"dégat(s)")

                elif dégats_joueur > dégats_monstre :
                    pv_monstre -= (dégats_joueur - dégats_monstre)
                    print ("Vous avez infligé", dégats_joueur - dégats_monstre ,"dégat(s) au monstre" )

                else :
                    print ("Égalité, personne ne subit de dégats")

            elif choix == "se défendre" :
                défense_joueur = random.randint (1,5)
                dégats_monstre = random.randint (1,5)

                if dégats_monstre > défense_joueur :
                    pv_joueur -= (dégats_monstre - défense_joueur)
                    print ("Vous avez subit", dégats_monstre - défense_joueur ,"dégat(s)")

                else :
                    pv_joueur += (défense_joueur - dégats_monstre)
                    print ("Vous avez récupéré", défense_joueur - dégats_monstre ,"PV")

            elif choix == "potion" :

                if max_potions > 0 :
                    soins_potion = random.randint (-6,6)
                    pv_joueur += soins_potion
                    max_potions -= 1

                    if soins_potion >= 0:
                        print ("Vous avez récupéré", soins_potion, "PV")

                    else :
                        print ("Vous vous êtes empoisonnés : vous perdez", soins_potion, "PV")
                else:
                    print ("Vous n'avez plus de potions")

            elif choix == "coup de ceinture":
                print ("Vous avez infligé", pv_monstre ,"dégat(s) au monstre" )
                pv_monstre = 0

            else:
                print("Vous ne pouvez pas faire ça")

        if pv_joueur <= 0 :
            print ("Vous avez perdu, le monstre a gagné")

        elif pv_monstre <= 0 :
            print ("Vous avez gagné, le monstre a perdu")

        else:
            pass

    elif difficulté == "giga chad":
        pv_joueur = random.randint(8,18)
        pv_monstre = random.randint(32,42)
        max_potions = 1
        dégats_joueur = 0
        dégats_monstre = 0
        défense_joueur = 0
        soins_potion = 0
        attaque_critique_joueur = 0
        attaque_critique_monstre = 0
        mod_easy = 1

        while pv_joueur > 0 and pv_monstre > 0 :
            print ("Vous avez", pv_joueur ,"PV")
            print ("Giga chad a", pv_monstre ,"PV")
            choix = str(input("Que voulez-vous faire ? attaquer, se défendre ou potion ")).lower()

            if choix == "mode easy" :
                if mod_easy > 0:
                    pv_joueur += 100
                    mod_easy -= 1
                else:
                    print("Mode déjà activé")

            elif choix == "attaquer" :
                dégats_joueur = int(random.randint (1,8))
                dégats_monstre = int(random.randint (6,25))
                attaque_critique_joueur = random.randint (1,15)
                attaque_critique_monstre = random.randint (1,3)

                if attaque_critique_joueur == 5 :
                    dégats_joueur *= 10
                elif attaque_critique_monstre == 2 :
                    dégats_monstre *= 3
                else:
                    pass

                if dégats_monstre > dégats_joueur :
                    pv_joueur -= (dégats_monstre - dégats_joueur)
                    print ("Vous avez subit", dégats_monstre - dégats_joueur ,"dégat(s)")

                elif dégats_joueur > dégats_monstre :
                    pv_monstre -= (dégats_joueur - dégats_monstre)
                    print ("Vous avez infligé", dégats_joueur - dégats_monstre ,"dégat(s) à Giga chad" )

                else :
                    print ("Égalité, personne ne subit de dégats")

            elif choix == "se défendre" :
                défense_joueur = random.randint (1,8)
                dégats_monstre = random.randint (1,10)

                if dégats_monstre > défense_joueur :
                    pv_joueur -= (dégats_monstre - défense_joueur)
                    print ("Vous avez subit", dégats_monstre - défense_joueur ,"dégat(s)")

                else :
                    pv_joueur += (défense_joueur - dégats_monstre)
                    print ("Vous avez récupéré", défense_joueur - dégats_monstre ,"PV")

            elif choix == "rage quit" :
                combat()
                
            elif choix == "potion" :

                if max_potions > 0 :
                    soins_potion = random.randint (-7,5)
                    pv_joueur += soins_potion
                    max_potions -= 1

                    if soins_potion >= 0:
                        print ("Vous avez récupéré", soins_potion, "PV")

                    else :
                        print ("Vous vous êtes empoisonnés : vous perdez", soins_potion, "PV")
                else:
                    print ("Vous n'avez plus de potions")

            elif choix == "coup de ceinture":
                print ("Vous avez infligé", pv_monstre ,"dégat(s) à Giga Chad" )
                pv_monstre = 0

            else:
                print("Vous ne pouvez pas faire ça")

        if pv_joueur <= 0 :
            print ("Giga Chad vous a HAGRAH")

        elif pv_monstre <= 0 :
            print ("Félicitations, vous avez vaincu Giga Chad")

        else:
            pass
    else :
        print("Cette difficulté n'existe pas")
        combat()

def combat1c1(pv_départ,dégats_de_base,défense_de_base):
    nom_joueur1 = input("Nom du joueur 1 : ")
    nom_joueur2 = input("Nom du joueur 2 : ")
    pv_joueur1 = int(pv_départ)
    pv_joueur2 = int(pv_départ)
    choix_joueur1=""
    choix_joueur2=""
    dégats_joueur1 = 0
    dégats_joueur2 = 0
    défense_joueur1 = int(défense_de_base)
    défense_joueur2 = int(défense_de_base)
    attaque_critique_joueur1 = 0
    attaque_critique_joueur2 = 0

    while pv_joueur1 > 0 and pv_joueur2 > 0 :
        print (nom_joueur1, "a", pv_joueur1 ,"PV")
        print (nom_joueur2, "a", pv_joueur2 ,"PV")
        choix_joueur1 = str(input(f"Que voulez-vous faire {nom_joueur1} ? attaquer ou se défendre ")).lower()
        if choix_joueur1 != "attaquer" and choix_joueur1 != "se défendre":
            print (nom_joueur1, "vous ne pouvez pas faire ça")
        else:
            choix_joueur2 = str(input(f"Que voulez-vous faire {nom_joueur2} ? attaquer ou se défendre ")).lower()
        if choix_joueur2 != "attaquer" and choix_joueur2 != "se défendre":
            print (nom_joueur2, "vous ne pouvez pas faire ça")

        elif choix_joueur1 == "attaquer" and choix_joueur2 == "attaquer" :
            dégats_joueur1 = random.randint (int(dégats_de_base),int(dégats_de_base)+10)
            dégats_joueur2 = random.randint (int(dégats_de_base),int(dégats_de_base)+10)
            attaque_critique_joueur1 = random.randint (1,10)
            attaque_critique_joueur2 = random.randint (1,10)

            if attaque_critique_joueur1 == 5 :
                dégats_joueur1 *= 2
            elif attaque_critique_joueur2 == 5 :
                dégats_joueur2 *= 2
            else:
                pass

            if dégats_joueur1 > dégats_joueur2 :
                pv_joueur2 -= (dégats_joueur1 - dégats_joueur2)
                print (nom_joueur2,"a subit", dégats_joueur1 - dégats_joueur2 ,"dégat(s)")

            elif dégats_joueur2 > dégats_joueur1 :
                pv_joueur1 -= (dégats_joueur2 - dégats_joueur1)
                print (nom_joueur1,"a subit", dégats_joueur2 - dégats_joueur1 ,"dégat(s)")

            else :
                print ("Égalité, personne ne subit de dégats")

        elif choix_joueur1 == "attaquer" and choix_joueur2 == "se défendre" :
            dégats_joueur1 = random.randint (int(dégats_de_base),int(dégats_de_base)+10)
            défense_joueur2 = random.randint (int(défense_de_base),int(défense_de_base)+10)

            if dégats_joueur1 > défense_joueur2 :
                pv_joueur2 -= (dégats_joueur1 - défense_joueur2)
                print (nom_joueur2 ,"a subit", dégats_joueur1 - défense_joueur2 ,"dégat(s)")

            elif défense_joueur2 > dégats_joueur1 :
                pv_joueur2 += (défense_joueur2 - dégats_joueur1)
                print (nom_joueur2 ,"a récupéré", défense_joueur2 - dégats_joueur1 ,"PV")

            else:
                print("Egalité, les PV ne changent pas")

        elif choix_joueur1 == "se défendre" and choix_joueur2 == "attaquer":
            défense_joueur1 = random.randint (int(défense_de_base),int(défense_de_base)+10)
            dégats_joueur2 = random.randint (int(dégats_de_base),int(dégats_de_base)+10)

            if dégats_joueur2 > défense_joueur1 :
                pv_joueur1 -= (dégats_joueur2 - défense_joueur1)
                print (nom_joueur1 ,"a subit", dégats_joueur2 - défense_joueur1 ,"dégat(s)")

            elif défense_joueur1 > dégats_joueur2 :
                pv_joueur1 += (défense_joueur1 - dégats_joueur2)
                print (nom_joueur1 ,"a récupéré", défense_joueur1 - dégats_joueur2 ,"PV")

            else:
                print("Egalité, les PV ne changent pas")

        elif choix_joueur1 == "se défendre" and choix_joueur2 == "se défendre":
            défense_joueur1 = random.randint (int(défense_de_base),int(défense_de_base)+5)
            défense_joueur2 = random.randint (int(défense_de_base),int(défense_de_base)+5)
            if défense_de_base < 0 :
                pv_joueur1 += (défense_joueur1 * -1)
                pv_joueur2 += (défense_joueur2 * -1)
                print(nom_joueur1 ,"a récupéré", défense_joueur1*-1, "PV")
                print(nom_joueur2 ,"a récupéré", défense_joueur2*-1, "PV")
            else:
                pv_joueur1 += défense_joueur1
                pv_joueur2 += défense_joueur2
                print(nom_joueur1 ,"a récupéré", défense_joueur1, "PV")
                print(nom_joueur2 ,"a récupéré", défense_joueur2, "PV")

        else:
            pass

    if pv_joueur1 <= 0 :
        print (nom_joueur1, "a succombé,", nom_joueur2, "a gagné")

    elif pv_joueur2 <= 0 :
       print (nom_joueur2, "a succombé,", nom_joueur1, "a gagné")

    else:
        pass

combat()