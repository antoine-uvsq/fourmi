# -*- coding: utf-8 -*-

import time
from tkinter import *
from random import choice
import sys
fenetre=Tk()
#on lui donne un titre
fenetre.title("Fourmi de Langton")
#on definit la fourmi par sa position et son sens

fourmi=[choice(list(range(0,10))),choice(list(range(0,10))),choice(['n','s','e','o'])]
jeu=Canvas(fenetre, width=400, height=400, bg='white')
plateau=[[choice(["black","white"]) for i in range(0,100)] for y in range(0,100)]
#on l'affiche
jeu.pack()

def dessinerplateau():
    global jeu,plateau
    for i in range(10):
        for j in range(10):
            #On calcul la taille du carré pour chaque tuile, ie les coordonnées
            jeu.create_rectangle((40*j, 40*i), (40*j+40, 40*i+40), fill=plateau[i][j])
def placerfourmi():
    global fourmi
    i=fourmi[0]
    j=fourmi[1]
    d=fourmi[2]
    global jeu
    #jeu.create_rectangle((40*j, 40*i), (40*j+40, 40*i+40), fill='red')
    if d=='n':
        jeu.create_text((40*j+20, 40*i+20), text='⇡', fill="red",font=('Helvetica','30','bold'))
    if d=='s':
        jeu.create_text((40*j+20, 40*i+20), text='⇣', fill="red",font=('Helvetica','30','bold'))
    if d=='e':
        jeu.create_text((40*j+20, 40*i+20), text='⇢', fill="red",font=('Helvetica','30','bold'))
    if d=='o':
        jeu.create_text((40*j+20, 40*i+20), text='⇠', fill="red",font=('Helvetica','30','bold'))
def action():
    global fourmi,plateau,jeu
    i,y=fourmi[0],fourmi[1]
    print(fourmi)
    if fourmi[2]=='n':
        if plateau[i][y]=='black':
            fourmi[2]='o'
            plateau[i][y]='white'
            if i==0:
                fourmi[0]=9
            else:
                fourmi[0]-=1
        else:
            fourmi[2]='e'
            plateau[i][y]='black'
            if i==0:
                fourmi[0]=9
            else:
                fourmi[0]-=1
    elif fourmi[2]=='s':
        if plateau[i][y]=='black':
            fourmi[2]='e'
            plateau[i][y]='white'
            if i==9:
                fourmi[0]=0
            else:
                fourmi[0]+=1
        else:
            fourmi[2]='o'
            plateau[i][y]='black'
            if i==9:
                fourmi[0]=0
            else:
                fourmi[0]+=1
    elif fourmi[2]=='o':
        if plateau[i][y]=='black':
            fourmi[2]='n'
            plateau[i][y]='white'
            if y==0:
                fourmi[1]=9
            else:
                fourmi[1]-=1
        else:
            fourmi[2]='s'
            plateau[i][y]='black'
            if y==0:
                fourmi[1]=9
            else:
                fourmi[1]-=1
    else:
        if plateau[i][y]=='black':
            fourmi[2]='s'
            plateau[i][y]='white'
            if y==9:
                fourmi[1]=0
            else:
                fourmi[1]+=1
        else:
            fourmi[2]='n'
            plateau[i][y]='black'
            if y==9:
                fourmi[1]=0
            else:
                fourmi[1]+=1
    print(fourmi)
    dessinerplateau()
    placerfourmi()
def play():
    global jeu
    while(True):
        action()
        jeu.update_idletasks()
        time.sleep(1)      

choix=Frame(fenetre)
Supp= Button(fenetre,text='Play', bg='green',width=5,command=play).pack(side=LEFT)
Supp= Button(fenetre,text='Pause', bg='blue',width=5).pack(side=LEFT)
Supp= Button(fenetre,text='Next', bg='purple',width=5,command=action).pack(side=LEFT)
choix.pack()
dessinerplateau()
placerfourmi()
#on affiche la fenetre
fenetre.mainloop()