from random import * #module random permettant de tirer au sort

def jeu(booléan): #paramètre booléan permettant d'indiquer si le jeu en question est un tiebreak ou non
    '''fonction prenant en paramètre un booléan permettant d'indiquer si le jeu en question est un tiebreak ou non et qui renvoie un tableau indiquant le gain ou non du jeu pour chaque joueur
    (forcément un vainqueur, représenté par la valeur 1 et un perdant, représenté par la valeur 0)'''
    pts_A = 0 #initialise les points du joueur A dans le jeu
    pts_B = 0 #initialise les points du joueur B dans le jeu
    proba=[0,1,2,3,4,5,6,7,8,9] #j'ai voulu tester de modifier les proba que A ou B gagne le point mais seuls le 0 et le 1 sont utiles

    if booléan: #si le jeu est un tiebreak 
        while (pts_A < 7 and pts_B < 7) or (pts_A - pts_B < 2 and pts_B - pts_A < 2): #tant qu'un des joueurs n'a pas remporté 7 points ou qu'il n'y a pas un différence de deux points (si 6-6)
            if proba[0] == randint(proba[0],proba[1]) :#tirage au sort du vainqueur du point
                pts_A+=1 #ajoute un point au joueur A
            else: #si le joueur B remporte le point
                pts_B+=1 #ajoute un point au joueur B

    else: #si c'est jeu classique (avec 15-30-40)
        while (pts_A < 4 and pts_B < 4) or (pts_A - pts_B < 2 and pts_B - pts_A < 2): #tant qu'un des joueurs n'a pas remporté 4 points ou qu'il n'y a pas un différence de deux points (si 3-3)
            if proba[0] == randint(proba[0],proba[1]) :#tirage au sort du vainqueur du point
                pts_A+=1 #ajoute un point au joueur B
            else: #si le joueur B remporte le point
                pts_B+=1 #ajoute un point au joueur B

    if pts_A > pts_B : #si le joueur A a remporté le jeu
        return [1,0] #on renvoie la valeur 1 à l'indice 0 pour indiquer que le joueur A a remporté le jeu
    else: #si le joueur B a remporté le jeu
        return [0,1] #on renvoie la valeur 1 à l'indice 1 pour indiquer que le joueur B a remporté le jeu
        
def set():
    '''fonction qui renvoie un tableau indiquant le gain ou non du set pour chaque joueur
    (forcément un vainqueur, représenté par la valeur 1 et un perdant, représenté par la valeur 0) ainsi que le nombre de jeu(x) remporté(s) par chaque joueur'''

    jeux_A=0 #initialise les jeux du joueur A dans le set
    jeux_B=0 #initialise les jeux du joueur B dans le set

    while (jeux_A < 6 and jeux_B < 6): #tant qu'aucun des deux joueurs n'a remporté le set ou qu'il n'y a pas de tiebreak (6-6)
            if jeux_A == 5 and jeux_B == 5: #si le score est de 5-5 (pour qu'il y ait 7-5 ou 6-6)
                jeu_x = jeu(False) #stockage du résultat du 11ème jeu (6-5 ou 5-6)
                jeux_A += jeu_x [0] #ajoute au compteur du joueur A l'éventuel jeu remporté (valeur 0 sinon)
                jeux_B += jeu_x [1] #ajoute au compteur du joueur A l'éventuel jeu remporté (valeur 0 sinon)

                jeu_x = jeu(False) #stockage du résultat du 12ème jeu (7-5 ou 5-7 ou 6-6)

            else: #si le score n'est pas de 5-5 (1-0, 2-2, etc.)
                jeu_x = jeu(False) #stockage du résultat du n-ième jeu

            jeux_A += jeu_x [0] #ajoute au compteur du joueur A l'éventuel jeu remporté (valeur 0 sinon)
            jeux_B += jeu_x [1] #ajoute au compteur du joueur B l'éventuel jeu remporté (valeur 0 sinon)

    if jeux_A == jeux_B: #si le score est de 6-6
        tiebreak=jeu(True) #stockage du résultat du tiebreak, déclenché par le paramètre True
        jeux_A += tiebreak[0] #ajoute au compteur du joueur A l'éventuel tiebreak remporté (valeur 0 sinon)
        jeux_B += tiebreak[1] #ajoute au compteur du joueur A l'éventuel tiebreak remporté (valeur 0 sinon)

    if jeux_A > jeux_B : #si le joueur A remporte le set
        return [1,0,jeux_A,jeux_B] #on renvoie la valeur 1 à l'indice 0 pour indiquer que le joueur A a remporté le set, ainsi que le score exact pour l'affichage final
    else: #si le joueur B remporte le set
        return [0,1,jeux_A,jeux_B] #on renvoie la valeur 1 à l'indice 1 pour indiquer que le joueur B a remporté le set, ainsi que le score exact pour l'affichage final
    
def match(nb_sets_gagnants,nom_joueur_A,nom_joueur_B):
    '''fonction prenant en paramètre un entier permettant d'indiquer le nombre de set(s) à remporter ainsi que les noms des joueurs, et qui affiche le vainqueur du match ainsi que le score détaillé'''

    sets_A = 0 #initialise les sets du joueur A dans le match
    sets_B = 0 #initialise les sets du joueur B dans le match
    score=[] #initialise le tableau d'affichage du score final

    while sets_A < nb_sets_gagnants and sets_B < nb_sets_gagnants : #tant qu'aucun des deux joueurs n'a remporté le match, soit le nombre de sets requis
        set_x=set() #stockage du résultat du set
        score.append(set_x[2]) #ajoute au tableau d'affichage du score le nombre de jeux remportés par le joueur A
        score.append(set_x[3]) #ajoute au tableau d'affichage du score le nombre de jeux remportés par le joueur B
        sets_A += set_x[0] #ajoute au compteur du joueur A l'éventuel set remporté (valeur 0 sinon)
        sets_B += set_x[1] #ajoute au compteur du joueur B l'éventuel set remporté (valeur 0 sinon)

    if sets_A > sets_B: #si le joueur A remporte le match, donc qu'il a plus de sets que le joueur B
        print(nom_joueur_A,"a battu",nom_joueur_B, sets_A,"set(s) à ",sets_B," : ", end=" ") #affichage de la victoire du joueur A (end=" " permettant de tout mettre sur la même ligne)
        i_bonus=0

    else: #si le joueur B remporte le match
        print(nom_joueur_B,"a battu",nom_joueur_A,sets_B,"set(s) à ",sets_A," : ",end=" ") #affichage de la victoire du joueur B
        i_bonus=1 #sert juste à ne mettre la boucle qu'une seule fois et à éviter les redondances dans le code (difficile à expliquer)

    for i in range(len(score)): #tant que tout le tableau d'affichage n'a pas été parcouru
        if i % 2 == 0: #si i est pair
            print(score[i+i_bonus]," - ",end=" ") #affiche le n-ième nombre de jeux du tableau de score (- séparant les nombres de jeux des joueurs), pour un affichage plus lisible
        else: #si i est impair
            print(score[i-i_bonus],end="  ") #affiche le n-ième nombre de jeux du tableau de score (sans - car fin du score de ce set)

match(3,"Medvedev","Sinner")