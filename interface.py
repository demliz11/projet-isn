# -*- coding: utf-8 -*-
# script Finch.py
#(C) auteur(e): Demay Lise

# On importe tkinter
from tkinter import * 
# Ici on importe tout les modules et bibliothèques dont on aura besoin
import tkinter.filedialog # message pour le outon quitter
from tkinter.messagebox import *
from tkinter import font #bibliothèque pour déterminer la police
from tkinter.colorchooser import * #voir couleur led
import os

# **************************************************************************

#On crée une fonction Toplevel définissant la fenêtre principale contenant 
def top():
    #on créer une fonction qui lie le clavier au boutons de l'interface pour faire aussi
    
    #création fenêtre
    Mafenetre=tkinter.Toplevel()
    Mafenetre.title("interface Finch")
    
    #définition de la taille de la fenêtre
    Mafenetre.geometry("1200x650")
    Mafenetre.maxsize(width=1050, height=650)
    Mafenetre.aspect(3, 2, 5, 3)
    #définition_de_la_couleur_de_fond
    Mafenetre['bg']='SlateGray1'     
    
    #apparition fenêtre
    Mafenetre.grab_set()#la fenêtre 2 apparaît devant la fenêtre 1
    Mafenetre.focus_set()  
    
    #on crée un menu
 
    menubar = Menu(Mafenetre)
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="A propros")
    menu1.add_command(label="Licence")
    menu1.add_separator()
    menubar.add_cascade(label="Informations", menu=menu1)
    
    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Utilisation du Finch")
    menu2.add_command(label="liens")
    menu2.add_separator()
    menubar.add_cascade(label="Aide", menu=menu2)
    
    Mafenetre.config(menu=menubar)
    
    # Création d'un widget Label (texte 'Bienvenu dans l'interface Finch !')
    
    Label1 = Label(Mafenetre, text = "Interface Finch!", font=("Arial", 15, "bold","italic"),
                   fg='mint cream', bg='light sea green', width=25, padx=40, pady=10)
  
    # Positionnement du widget avec la méthode grid
    Label1.grid(row=0, column=24)
 
    #************************************************************************
    
    #création canvas boutons direction 
    
    #définition des fonctions pour lier le clavier au boutons de l'interface
    def gauche():
        message="gauche"
       
        print (message)
    
    def droite():
        message2="droite"
        print (message2)
        
    def avance():
        message3="avance"
        print (message3)
    
    def recul():
        message4="recul"
        print (message4)
        
    def stop():
        message5="stop"
        print (message5)
     
    
    #************************************************************************
    
    #bouton aller à droite
    can = Canvas(Mafenetre, width=100, height=90, bg="SlateGray1" ,  highlightthickness=0)
    can.grid(column=14, row=11)
    
    Bouton= Button(Mafenetre, width=2, background='black', activebackground="black",command=droite)
    Bouton= can.create_window(60, 45, window=Bouton)
    
    pts = [(10,45),(80,80),(80,10)]
    
    can.create_polygon(pts, fill="black", outline="black", width=3)
    
    #bouton aller à gauche
    can1 = Canvas(Mafenetre, width=100, height=90, bg="SlateGray1",  highlightthickness=0)#highlightthickness=0 signifie que le contour gris autour du widget est inexistant
    can1.grid(column=20, row=11)
    Boutongauche= Button(Mafenetre, width=2, background='black', activebackground="black", command=gauche)
    Boutongauche= can1.create_window(40, 40, window=Boutongauche)  
    pts = [(80,45),(10,80),(10,10)]  
    can1.create_polygon(pts, fill="black", outline="black", width=3)#afficher le polygone dans le canvas
    
    #bouton recul
    
    can2 = Canvas(Mafenetre, width=90, height=100, bg="SlateGray1",  highlightthickness=0)
    can2.grid(column=15, row=12)
    Boutonrecul= Button(Mafenetre, width=2, background='black', activebackground="black", command=recul)
    Boutonrecul= can2.create_window(50, 35, window=Boutonrecul)
    
    pts = [(10,10),(45,80),(80,10)]
    
    can2.create_polygon(pts, fill="black", outline="black", width=3)
    
    #bouton avancer
    can3 = Canvas(Mafenetre, width=90, height=100, bg="SlateGray1",  highlightthickness=0)
    can3.grid(column=15, row=10)
    Boutonavancer= Button(Mafenetre, width=2, background='black', activebackground="black", command=avance)
    Boutonavancer= can3.create_window(50, 50, window=Boutonavancer)
    
    pts = [(10,80),(45,10),(80,80)]
    
    can3.create_polygon(pts, fill="black", outline="black", width=3)
    
    #****************************************************************************
    #bouton stop
    boutonstop=tkinter.Button(Mafenetre, width=10, text="STOP", font=" bold", height= 4, bg="SlateBlue2", 
                              activebackground="SlateBlue3", fg='white', command=stop).grid(row=11, column=15)
 
    #définition du call back pour le bouton quitter
    def callback():
        if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
            showwarning('Titre 2', 'Tant pis...')
            racine.destroy()
            Mafenetre.destroy()
        else:
            showinfo('Titre 3', 'Rebonjour')
    
    #création bouton quitter
    boutonquitter=tkinter.Button(Mafenetre, text='Quitter',width=15, bg='MediumPurple1', 
                                 activebackground="MediumPurple2", height=2, command = callback)
    boutonquitter.grid(row=17, column=25)

     #****************************************************************************
     #Accélération Finch  
    def maj(nouvelleValeur):
        # nouvelle valeur en argument
        print(nouvelleValeur)
    
    #création Frame l'entourant
    Frame3= Frame(Mafenetre, borderwidth=2, relief=GROOVE, bg="lavender", highlightbackground="lavender",
                  highlightcolor="lavender blush", highlightthickness=10, bd=0, width=200, height=200)
    
    #création barre
    Valeur = StringVar()
    Valeur.set(50)
    
    # Création d'un widget Scale
    echelle = Scale(Frame3,from_=-100,to=100,resolution=10,orient=HORIZONTAL,\
    length=300,width=20,label="Accélération Finch",tickinterval=20,variable=Valeur,bg="white", command=maj)
    echelle.grid(row=21, column=26)
    Frame3.grid(row=17, column=24)
    
    #****************************************************************************
    # réglage vitesse
    
    Frame1= Frame(Mafenetre,borderwidth=2, relief=GROOVE, bg="medium turquoise", highlightbackground="medium turquoise", 
                  highlightcolor="RoyalBlue1",highlightthickness=3, bd=0, width=300, height=400, padx=20) 
    
    Frame2= Frame(Frame1, borderwidth=2, relief=GROOVE, bg="pale turquoise", highlightbackground="pale turquoise", 
                  highlightcolor="RoyalBlue1",highlightthickness=3, bd=0, width=200, height=300)
    
    Frame1.grid(row=17, column=15)
    
    Frame2.grid(row=2, column=3)
    
    Label(Frame2, text="vitesse Finch", bg="pale turquoise", font=("bold")).grid(row=0, column=1)                          

    #***********************************************************************************
    #checkbuttons sélection vitesse
    var=IntVar()
    
    Vite=tkinter.Radiobutton(Frame2, text="rapide", variable= var, value=1, bg="pale turquoise").grid(row=1, column=0)
    Moyen=tkinter.Radiobutton(Frame2, text="modéré", variable=var, value=2, bg="pale turquoise").grid(row=2, column=0)
    Lent=tkinter.Radiobutton(Frame2, text="lent", variable=var, value=3, bg="pale turquoise").grid(row=3, column=0)

    #****************************************************************************
    #choix couleur led
    #création d'un canva qui contient les boutons
    couleur = Canvas(Mafenetre, width=210, height=100, bg="white" , borderwidth=5, highlightthickness=0 )
    couleur.grid(row=11, column=24)
    
    # titre
    Label3 = Label(Mafenetre, text ="Sélection des couleurs de la led",font=("Arial", 10, "bold"), fg = 'black', bg="white")
    Label3 = couleur. create_window(110, 15, window=Label3)
  
    #****************************************************************************
    #boutons
    
    #led rose
    rose= Button(Mafenetre, background='hot pink', activebackground="HotPink1", width=2, height=1)
    rose= couleur.create_window(25, 50, window=rose)
    #led bleu
    bleu= Button(Mafenetre, background='DodgerBlue2', activebackground="DodgerBlue3", width=2, height=1)
    bleu= couleur.create_window(55, 50, window=bleu)
    #led verte
    vert= Button(Mafenetre, background='dark sea green', activebackground="DarkSeaGreen2", width=2, height=1)
    vert= couleur.create_window(55, 90, window=vert)
    #led rouge
    rouge= Button(Mafenetre, background='red', width=2, activebackground="red3", height=1)
    rouge= couleur.create_window(85, 50, window=rouge)
    #led violette
    violet= Button(Mafenetre, background='SlateBlue2', activebackground="SlateBlue3", width=2, height=1)
    violet= couleur.create_window(25, 90, window=violet)
    #led orange
    orange= Button(Mafenetre, background='dark orange', activebackground="DarkOrange2", width=2, height=1)
    orange= couleur.create_window(85, 90, window=orange)
    
    #**********************************************************************
    #demander sélection couleur
    def getColor():
        color = askcolor() 
        
        print (color)
        
    autre=Button(Mafenetre, text='Autre\n couleur', bg='lavender', font=( "bold"), command=getColor)
    autre=couleur.create_window(160, 65, window=autre)
    

    #########################################################################
    # Ajout label jeu labyrinthe
    
    jeu= Label(Mafenetre, text="Jeu labyrinthe", font="bold", fg = 'SlateBlue2', bg='SlateGray1')
    jeu.grid(row=10, column=25)
    
    # Ajout image
        
    laby= tkinter.PhotoImage(file="imagelab.gif")
    lab = Label(Mafenetre,width=200, height=185, image=laby)
    lab.laby=laby
    lab.grid(row=11, column=25)
     
    
    #****************************************************************************
    #création d'un bouton reliant l'interface au jeu labyrinthe
    
    #création d'un bouton reliant l'interface au jeu labyrinthe
    #fonction ouvrant le fichier 
    def laby():
        
        
        #**************lien autre programme***********
        os.system('labyrinthe.py')#ouverture du jeu
        #*********************************************
       
    photo= PhotoImage(file="tresor.gif")
    maze= Button(Mafenetre, width=70, height=25, image=photo, command= laby)
    maze.photo = photo
    maze.grid(row=16, column=25)
        
        
 
#****************************************************************************
#création fenêtre d'accueil

racine=tkinter.Tk()
racine.title("ouverture")
racine.geometry("500x250")
racine.maxsize(width=500, height=250)

can=Canvas(racine,width=500,height=200,bg='white')
image1 = PhotoImage(file="imagefinch.gif")
 
can.create_image(250,100,image=image1)
can.pack()

 # bouton redirigeant sur la page numéro 2 quand on clique dessus
 
bouton=tkinter.Button(racine, text="Bienvenue", relief="sunken", borderwidth=5,font="helvetica 20 bold", fg='white', bg='MediumOrchid4',  
                      activebackground="DarkOrchid4",command=top)
bouton.pack(side="bottom",fill="both", expand=1)

racine.mainloop()
