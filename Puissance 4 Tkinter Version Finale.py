def partie():
    largeur = 7
    hauteur = 6
    jetons = ['O', 'X']
    nb_coups = 0
    gagnant = -1
    grille = initialiser_grille(largeur)
    while nb_coups < largeur * hauteur :
        afficher_grille(grille, hauteur)
        c, h = poser_jeton(grille, hauteur, joueur, jetons)
        nb_coups = nb_coups + 1
        if alignement(grille, c, h):
            gagnant = joueur
            break
        joueur = 1 - joueur
    afficher_grille(grille, hauteur)
    if gagnant == -1:
        print('partie nulle')
    else:
        print(jetons[gagnant], 'a gagné')

def poser_jeton(grille, hauteur, joueur, jetons ):
    '''affiche le joueur dont cest le tour de jeu'''
    print( "cest le tour de " , joueur )

    ''' On initialise la variable colonne'''
    condition_colonne_valide = False
    condition_colonne_numerique = False
    condition_range_colonne = False
    condition_colonne_non_remplie = False

    '''verif le nombre est compris entre 1 et nombre colonnes'''
    while not condition_colonne_valide:

        '''demander le numéro de colonne ou deposer jeton'''
        colonne = input('numero de la colonne ')

        ''' Verifier que la colonne est numerique '''
        if not colonne.isnumeric():
            print('la colonne indiquee nest pas numerique ')
            condition_colonne_numerique = False
        else:
            ''' Conversion de colonne en integer '''
            colonne = int(colonne)
            condition_colonne_numerique = True

            if not (colonne >=1 and colonne <= len(grille)):
                print('la colonne indiquee nest pas entre 1 et ', len(grille))
                condition_range_colonne = False
            else:
                condition_range_colonne = True

                ''' Verifier que la colonne n est pas remplie '''
                if len(grille[colonne-1]) >= hauteur :
                    print('la colonne est deja remplie')
                    condition_colonne_non_remplie = False
                else:
                    condition_colonne_non_remplie = True

        ''' Verifier que toutes les conditions sont remplies '''
        condition_colonne_valide = condition_colonne_numerique and condition_range_colonne and condition_colonne_non_remplie
    ''' jeton ajoute dans la colonne choisie '''
    grille[colonne-1].append(jetons[joueur])
    return colonne-1, len(grille[colonne-1])-1


def alignes_dir(grille, c, h, delta_h, delta_v):
    nb1=0
    nb2=0
    jeton1='X'
    jeton2='O'
    if grille[c][h]==jeton1:
        if delta_h==-1:
            if grille[c-1][h]==jeton1:
                nb1+=1
                if grille[c-2][h]==jeton1:
                    nb1+=1
                    if grille[c-3][h]==jeton1:
                        nb1+=1
        elif delta_h==1:
            if grille[c+1][h]==jeton1:
                nb1+=1
                if grille[c+2][h]==jeton1:
                    nb1+=1
                    if grille[c+3][h]==jeton1:
                        nb1+=1
        if delta_v==-1:
            if grille[c][h-1]==jeton1:
                nb1+=1
                if grille[c][h-2]==jeton1:
                    nb1+=1
                    if grille[c][h-3]==jeton1:
                        nb1+=1
        elif delta_v==1:
            if grille[c][h+1]==jeton1:
                nb1+=1
                if grille[c][h+2]==jeton1:
                    nb1+=1
                    if grille[c][h+3]==jeton1:
                        nb1+=1
    elif grille[c][h]==jeton2:
        if delta_h==-1:
            if grille[c-1][h]==jeton2:
                nb2+=1
                if grille[c-2][h]==jeton2:
                    nb2+=1
                    if grille[c-3][h]==jeton2:
                        nb2+=1
        elif delta_h==1:
            if grille[c+1][h]==jeton2:
                nb2+=1
                if grille[c+2][h]==jeton2:
                    nb2+=1
                    if grille[c+3][h]==jeton2:
                        nb2+=1
        if delta_v==-1:
            if grille[c-1][h]==jeton2:
                nb2+=1
                if grille[c-2][h]==jeton2:
                    nb2+=1
                    if grille[c-3][h]==jeton2:
                        nb2+=1
        elif delta_v==1:
            if grille[c][h+1]==jeton2:
                nb2+=1
                if grille[c][h+2]==jeton2:
                    nb2+=1
                    if grille[c][h+3]==jeton2:
                        nb2+=1
    if nb1>nb2:
        return nb1
    else:
        return nb2
    return nb1,nb2

def alignement(grille, c, h):
    al_horizontal1=0
    al_vertical1=0
    al_diagonal1=0
    al_horizontal2=0
    al_vertical2=0
    al_diagonal2=0
    jeton1='X'
    jeton2='O'
    if grille[c][h]==jeton1:
        while c<=7 and c>=0:
            for i in range(4):
                if grille[c+i][h]==jeton1:
                    al_horizontal1+=1
        while h<=6 and h<=0:
            for i in range(4):
                if grille[c][h+i]==jeton1:
                    al_vertical1+=1
        while c<=7 and c>=0 and h<=6 and h<=0:
            for i in range(4):
                if grille[c+i][h+i]==jeton1:
                    al_diagonal1+=1
    if grille[c][h]==jeton2:
        while c<=7 and c>=0:
            for i in range(4):
                if grille[c+i][h]==jeton2:
                    al_horizontal2+=1
        while h<=6 and h<=0:
            for i in range(4):
                if grille[c][h+i]==jeton2:
                    al_vertical2+=1
        while c<=7 and c>=0 and h<=6 and h<=0:
            for i in range(4):
                if grille[c+i][h+i]==jeton2:
                    al_diagonal2+=1
    if al_horizontal1==4:
        label['text'] ='alignement horizontal rouge'
    elif al_vertical1==4:
        label['text'] ='alignement vertical rouge'
    elif al_diagonal1==4:
        label['text'] ='alignement diagonal rouge'
    elif al_horizontal2==4:
        label['text'] ='alignement horizontal jaune'
    elif al_vertical2==4:
        label['text'] ='alignement vertical jaune'
    elif al_diagonal2==4:
        label['text'] ='alignement diagonal jaune'

from tkinter import*
import random as rd
import tkinter as tk
grille=[[],[],[],[],[],[],[]]
fen=tk.Tk()
fen.title('Puissance 4')
fen.geometry('1200x800')
fen.configure(bg='gray')
a=0#variable permettant d'alterner entre le rouge et le jaune
canevas=tk.Canvas()
canevas.configure(bg='blue',width=900,height=720)
canevas.pack()

for i in range(100,800,100):
    for j in range(100,700,100):
        canevas.create_oval(10+i,11+j,100+i,101+j,fill='white')#création de la grille
label = tk.Label(fen, text="C'est aux rouges de jouer")
label.config(font=("Courier", 20))
label.pack(pady=10)

def poser_dans_colonne(c):
    global a,grille
    b=len(grille[c-1])
    if a<41:#limite le nombre de jetons possibles à 42 (6x7)
        if b<6:
            if a%2==0 :
                label['text'] = "C'est aux jaunes de jouer"
                canevas.create_oval(10+(100*c),11+(600-b*100),100+(100*c),101+(600-b*100),fill='red')
                a+=1
                grille[c-1].append('X')
            else:
                label['text'] = "C'est aux rouges de jouer"
                canevas.create_oval(10+(100*c),11+(600-b*100),100+(100*c),101+(600-b*100),fill='yellow')
                a+=1
                grille[c-1].append('O')
    elif a==41:#lorsque toutes les cases sont remplies
        label['text'] = "Partie Nulle"
        canevas.create_oval(10+(100*c),11+(600-b*100),100+(100*c),101+(600-b*100),fill='yellow')
        a+=1
        grille[c-1].append('O')
    else:
        fen.destroy()

bouton1=tk.Button(fen,text=' 1 ',command=lambda:poser_dans_colonne(1))
bouton2=tk.Button(fen,text=' 2 ',command=lambda:poser_dans_colonne(2))
bouton3=tk.Button(fen,text=' 3 ',command=lambda:poser_dans_colonne(3))
bouton4=tk.Button(fen,text=' 4 ',command=lambda:poser_dans_colonne(4))
bouton5=tk.Button(fen,text=' 5 ',command=lambda:poser_dans_colonne(5))
bouton6=tk.Button(fen,text=' 6 ',command=lambda:poser_dans_colonne(6))
bouton7=tk.Button(fen,text=' 7 ',command=lambda:poser_dans_colonne(7))
bouton1.place(x=293,y=50)
bouton2.place(x=393,y=50)
bouton3.place(x=493,y=50)
bouton4.place(x=593,y=50)
bouton5.place(x=693,y=50)
bouton6.place(x=793,y=50)
bouton7.place(x=893,y=50)

fen.mainloop()
