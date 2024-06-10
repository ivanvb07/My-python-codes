from tkinter import*
import random as rd
import tkinter as tk

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
