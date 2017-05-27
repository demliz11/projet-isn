# -*- coding: utf-8 -*-
#auteur(e): demay Lise
# Voici un petit jeu modélisant représentant le finch dans un labyrinthe virtuel

import turtle 
#notre module de référence basé sur la librairie tkinter
import math
import random 
import winsound

wn= turtle.Screen() #création de la fenêtre
wn.bgcolor("black") #définition d'une couleur au cas ou l'image ne fonctionne pas
wn.title("Finch labyrinthe")
wn.setup(700,724) #taille de la fenêtre
wn.bgpic("im.gif") # image fond d'écran

#définir music de fond
#ne marche que sur windows avec winsound
#on aurait aussi pu utiliser pygame.mixer 
winsound.PlaySound("finch.wav",winsound.SND_ASYNC)  

#stop le display tant tout n'a pas été "updated"
wn.tracer(0)

#liste contenant les images
images= ["door.gif", "mur.gif", "finch.gif", "tresor.gif", "obsta.gif", "ennemi.gif", "mini.gif", "bas.gif", "dos.gif","droite.gif"]
for image in images :
    turtle.register_shape(image)

    
#créer labyrinthe
#création de classes 
class Pen(turtle.Turtle): # classe crayon= dessine murs du labyrinthe
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("mini.gif")
        self.penup() # le crayon se lève pour qu'on ne voit pas les traits 
        self.speed(0) # vitesse du jeu la plus rapide soit 0
        
#créer classe représentant le finch
class Finch(turtle.Turtle): # turtle.Turtle= tout ce que le module Turtle peut faire, Finch le peut (classe enfant)
    def __init__(self): #initialisation
        turtle.Turtle.__init__(self) #initialisation classe parent
        self.shape("droite.gif") 
        self.color("white")
        self.penup() #le crayon se lève
        self.speed(0) 
        self.gold=50
        self.vies=10 #nombre de vies au départ

    #**************************************************************************    
    #définition les mouvements du Finch    
    
    def haut(self):
        #calculer les coordonnées du futur emplacement du Finch
        move_to_x=finch.xcor()
        move_to_y=finch.ycor() + 24
        self.shape("dos.gif")#l'image change pour que le finch tourne le dos
        
        #vérifier si l'espace a un mur
        if (move_to_x, move_to_y) not in murs:
            self.goto(move_to_x, move_to_y)
        
    def bas(self):
        #calculer les coordonnées du futur emplacement du Finch
        move_to_x=finch.xcor()
        move_to_y=finch.ycor() - 24
        self.shape("bas.gif")
        
        #vérifier si l'espace a un mur
        if (move_to_x, move_to_y) not in murs:
            self.goto(move_to_x, move_to_y)
             
    def droite(self):
        #calculer les coordonnées du futur emplacement du Finch
        move_to_x=finch.xcor() + 24
        move_to_y=finch.ycor() 
        self.shape("droite.gif")
        
        #vérifier si l'espace a un mur
        if (move_to_x, move_to_y) not in murs:
            self.goto(move_to_x, move_to_y)
             
    def gauche(self):
        #calculer les coordonnées du futur emplacement du Finch
        move_to_x=finch.xcor() - 24
        move_to_y=finch.ycor() 
        self.shape("finch.gif")
        #vérifier si l'espace a un mur
        if (move_to_x, move_to_y) not in murs:
            self.goto(move_to_x, move_to_y)
    
    #définir fonction qui retourne si collision avec trésor
    def collision(self, autre):
        a=self.xcor()-autre.xcor()
        b=self.ycor()-autre.ycor()
        distance = math.sqrt((a**2)+(b**2)) #formule de Pythagore 
        if distance <5:
            return True #logique boléeenne
            #il y a une collision si True
        else:
            return False
    #definir fonction victoire
    
    
    
    #détruire Finch si un obstacle est touché
    def destroy(self):
        self.goto(1800,1800)
        self.hideturtle()
    
    
class Tresor(turtle.Turtle):
    #création de trésors pour rendre le Jeu plus amusant
    def __init__(self, x, y): #initialisation
        turtle.Turtle.__init__(self) #initialisation classe parent
        self.shape("tresor.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold=10 #valeur du trésor
        self.vies=1 #nombre de vies lorsque l'on trouve un trésor
        self.goto(x,y) # emplacement
    
    #définition d'une fonction détruisant le trésor quand le finch le trouve
    def destroy(self):
        self.goto(2000,2000) #emplacement trésor déplacé car avec turtle on ne peut pas vraiment détruire
        self.hideturtle()
        
#classe définissant des obstacles  mouvants
class Obstacle(turtle.Turtle):
    def __init__(self, x, y): #initialisation
        turtle.Turtle.__init__(self) #initialisation classe parent
        self.shape("obsta.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold=25 
        self.goto(x,y) # emplacement
        self.direction = random.choice(["haut","bas","gauche","droite"]) #liste des directions 
    
    #fonction définissant la direction des obstacles
    def mouvement(self):
        if self.direction=="haut":
            #l'obstacle se déplace vers le haut
            #d désigne delta
            dx=0
            dy=24
        elif self.direction=="bas":
            #l'obstacle se déplace vers le bas
            dx=0
            dy=-24
        elif self.direction=="gauche":
            #l'obstacle se déplace vers la gauche
            dx=-24
            dy=0
        elif self.direction=="droite":
            #l'obstacle se déplace vers la droite
            dx=24
            dy=0
        else:
            dx=0
            dy=0
        #calculer les coordonnéees du future emplacement de l'obstacle
        move_to_x=self.xcor() + dx
        move_to_y=self.ycor() + dy
            
        #vérifier si l'espace a un mur
        if (move_to_x, move_to_y) not in murs:
            self.goto(move_to_x, move_to_y)
        else:
            #changer de direction
            self.direction = random.choice(["haut","bas","gauche","droite"])
        
            
        #définir le temps entre les différentes actions
        turtle.ontimer(self.mouvement, t= random.randint(100,300)) 
        #random interval 100 -300  millisecondes= change la vitesse de l'obstacle
        
    #détruire l'obstacle
    def destroy(self):
        self.goto(1800,1800)
        self.hideturtle()
        
#création d'une classe pour la porte permettant la sortie du labyrinthe       
class Porte(turtle.Turtle):
    def __init__(self, x, y): #initialisation
        turtle.Turtle.__init__(self) #initialisation classe parent
        self.shape("door.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x,y)           
        #si le finch traverse la porte le niveau est gagné

        
#classe définissant les ennemis du Finch
class Ennemi(turtle.Turtle):
    def __init__(self, x, y): #initialisation
        turtle.Turtle.__init__(self) #initialisation classe parent
        self.shape("ennemi.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.vies=1
        self.goto(x,y) # emplacement
        self.direction = random.choice(["haut","bas","gauche","droite"]) #liste des directions 
        
    #fonction définissant la direction des obstacles
    def mouvement(self):
        
        if self.direction=="haut":
            #l'obstacle se déplace vers le haut
            #d désigne delta
            dx=0
            dy=24
        elif self.direction=="bas":
            #l'obstacle se déplace vers le bas
            dx=0
            dy=-24
        elif self.direction=="gauche":
            #l'obstacle se déplace vers la gauche
            dx=-24
            dy=0
        elif self.direction=="droite":
            #l'obstacle se déplace vers la droite
            dx=24
            dy=0
        else:
            dx=0
            dy=0
            
        #on souhaite que l'ennemi suive le finch sur une certaine distance
        #on doit calculer la distance du Finch à  l'ennemi 
        #voir plus bas fonction proche
        if self.proche(finch):
            if finch.xcor()< self.xcor():
                self.direction = "gauche"
            elif finch.xcor()>self.xcor():
                self.direction = "droite"
            elif finch.ycor()> self.ycor():
                self.direction= "haut"
            elif finch.ycor()<self.ycor():
                self.direction="bas"
       
        #calculer les coordonnéees du futur emplacement de l'ennemi
        move_to_x=self.xcor() + dx
        move_to_y=self.ycor() + dy
        
        #vérifier si l'espace a un mur ou un obstacle
        if (move_to_x, move_to_y) not in murs:
            self.goto(move_to_x, move_to_y)
        else:
            #changer de direction
            self.direction = random.choice(["haut","bas","gauche","droite"])
            
        #définir le temps entre les différentes actions
        turtle.ontimer(self.mouvement, t= random.randint(100,300)) 
        #random interval 100 -300 millisecondes= change la vitesse de l'obstacle
        
        
    #définir fonction qui calcule si le finch est proche de l'ennemi
    def proche(self, autre):
        a=self.xcor()-autre.xcor()
        b=self.ycor()-autre.ycor()
        distance = math.sqrt((a**2)+(b**2)) #formule de Pythagore 
        if distance <60: #environ 3 blocs éloignés
        
            return True #logique boléenne
            #il y a une collision si True
        else:
            return False                                                            
    
    #détruire l'obstacle
    def destroy(self):
        self.goto(1800,1800)
        self.hideturtle()

#création d'une classe comptabilisant le score du Finch
class Score(turtle.Turtle): 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("mini.gif")
        self.penup() # le crayon se lève pour qu'on ne voit pas les traits 
        self.speed(0) # vitesse du jeu la plus rapide soit 0
        self.pendown()
        
    #définition de la fonction affichant la quantité d'argent du Finch
    def argent(self):
        self.undo() # permet de défaire l'action précédante
        #la première fois le self.pendown() est défait donc le crayon est levé
        #à la seconde collision
        #le undo permet d'enlever l'affichage du score précédant se référant à "finch.gold" (dernière action)
        #les scores ne se superposent donc pas car le précédant est supprimé à chaque collision                         
        msg="l'argent du finch est:%s"%(finch.gold)
        self.penup()
        self.goto(-284, 280)
        self.write(msg, font=("Arial", 15, "bold"))        
        
#création d'une classe comptabilisant le nombre de vies du Finch
class Vie(turtle.Turtle): 
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("mini.gif")
        self.penup() # le crayon se lève pour qu'on ne voit pas les traits 
        self.speed(0) # vitesse du jeu la plus rapide soit 0
        self.pendown()
        
    #définition de la fonction affichant le nombre de vies du Finch
    def sante(self):
        self.undo()
        msg="nombre de vies du Finch:%s"%(finch.vies)
        self.penup()
        self.goto(30, 280)
        self.write(msg, font=("Arial", 15, "bold"))        
       
        
#créer liste niveaux

niveaux = [""]
#defir le niveau 1
niveau_1 = [
"                         ", 
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XF XXXXXXXO         XXXXX", #le F représente le Finch                         
"X  XXXXXXX  XXXXXX  XXXXX",
"X      OXX  XXXXXX  XXXXX",
"X       XX  XXX      T XX",
"XXXXXX  XX  XXXO       XX",# le O désigne l'obstacle mouvant
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX  E XXXX  XXXXX", #le E représente un ennemi du Finch
"X TXXX        XXXX  XXXXX", #le T représente le trésor
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"XE               XXXXXXXX",
"XXXXXXXXXXXX     XXXXXT X",
"XXXXXXXXXXXXXXX OXXXXX  X",
"XXXT XXXXXXXXXX         X",
"XXX                     X",
"XXX0        XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX T XXXXX            E X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XX        E XXXX        X",
"XXXX                    P", # P représente une porte
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#créeer une liste pour les différents trésors
tresors = []

#créer une liste pour les ennmis du Finch
ennemis = []

#créer une liste pour les portes
portes=[]

#ajouter 
niveaux.append(niveau_1)
#créeer fonction niveau

def labyrinthe(niveau):
    for y in range(len(niveau)):
        #y: ordonnées nombre de lignes de la liste 
    
        for x in range (len(niveau[y])):
            
            symbole = niveau[y][x]
            #calculer les coordonnées x,y
            #les blocs font 24 pixels de taille
            screen_x=-288 + (x * 24) # bloc x=0*24, x=1(position rang sur ligne)*24
            screen_y= 288 - (y*24) # - car on va de bas en haut
            
            # vérifier s'il y a un "X" (mur)
            if symbole=="X":
                pen.goto(screen_x, screen_y)#le crayon se déplace
                pen.shape("mur.gif")
                pen.stamp()# affichage des blocs
                #coordonner la liste des murs
                #but: empêcher que le Finch ne traverse les murs
                murs.append((screen_x, screen_y)) #tuple (explique les "()")
                
            #vérifier s'il y a un "F"( Finch)
            if symbole=="F":
                finch.goto(screen_x, screen_y) #emplacement Finch dans le labyrinthe
                
            #vérifier s'il y a un "T" (trésor)
            if symbole=="T":
                tresors.append(Tresor(screen_x, screen_y))
            
            #vérifier s'il y a un "O"(obstacle)
            if symbole=="O":
                obstacles.append(Obstacle(screen_x, screen_y))  
                
            #vérifier s'il y a un "E" (ennemi)
            if symbole=="E":
                ennemis.append(Ennemi(screen_x, screen_y))
                
            #vérifier s'il y a un "P" (porte de sortie)
            if symbole=="P":
                portes.append(Porte(screen_x, screen_y))
       
#créer instances classes
pen= Pen()
score=Score()
vie=Vie()

finch=Finch() #le personnage de notre jeu

#afficher le score
score.argent()
vie.sante()
# liste des murs
#but: éviter que le finch ne passe à  travers les murs du labyrinthe
murs=[]

obstacles=[]

#mettre en place le labyrinthe
labyrinthe(niveaux[1])
print (murs) #positions de tous les murs

#lier le clavier à  l'écran afin de diriger le finch avec les touches
turtle.listen()
turtle.onkey(finch.gauche, "Left") #"Left" désigne la flèche gauche clavier (on pourrait utiliser aussi "a")
turtle.onkey(finch.droite, "Right")
turtle.onkey(finch.haut, "Up")
turtle.onkey(finch.bas, "Down")

#stop le display tant tout n'a pas été updated"
wn.tracer(0)

#bouger les obstacles
for obstacle in obstacles:
    turtle.ontimer(obstacle.mouvement, t=250)# bougent aprés 250 
    
#bouger les ennemis
for ennemi in ennemis:
    turtle.ontimer(ennemi.mouvement, t=200) #t=200: vitesse des ennemis
    

#************************************************************************************************************
#boucle principale
#************************************************************************************************************

while True:

    #vérifier si le finch rencontre un trésor
    for tresor in tresors:
        if finch.collision(tresor):
            #ajouter l'argent du trésor à  celui du finch
            finch.gold += tresor.gold
            finch.vies += tresor.vies
            score.argent()
            #détruire le trésor
            tresor.destroy()
            #enlever le trésor de la liste des trésors
            tresors.remove(tresor)

    #définition d'une fonction faisant perdre de l'argent après un laps de temps
    #sinon le finch perd trop rapidement de l'argent
    def perte():
        finch.gold -=obstacle.gold        
    #s'il y a collision avec obstacle       
    for obstacle in obstacles:
        if finch.collision( obstacle):
            turtle.ontimer(perte,100)
            #la nouvelle quantité d'argent est mise à jour
            score.argent()

    #fonction faisant perdre des points de vie au finch
    def points():
        finch.vies-=ennemi.vies
    #si le finch rencontre un ennemi        
    for ennemi in ennemis:
        if finch.collision(ennemi):
            #le finch perd une vie
            turtle.ontimer(points,100)
            vie.sante()
      
    #Si le Finch n'a plus de vies, la partie est perdue
    # définition de quelques fonctions intervenant dans la boucle principale   
        #définir une fonction arrêtant l'écran lorsque le le jeu est perdu
    def arret():
        wn.reset()
        wn.bye()
    # fonction affichant une image quand le jeu est perdu   
    def fenetre():
        mn.bgpic("perdu.gif") 
               
    if finch.vies==0:
        winsound.PlaySound(None, winsound.SND_ASYNC)
        #le finch disparaît
        turtle.clearscreen() #l'écran redevient blanc
        mn= turtle.Screen() #création de la fenêtre
        #fermeture de l'écran
        turtle.ontimer(fenetre,5)
        turtle.ontimer(arret, 4000) # l'écran est fermé après 3 s
        
    # si le finch n'a plus d'argent il perd une vie
    if finch.gold==0:
        finch.vies-=1 #le finch perd une vie
        vie.sante()
    
    #si le finch trouve la porte de sortie    
    for porte in portes:
        if finch.collision(porte):
            winsound.PlaySound(None, winsound.SND_ASYNC)
            #le finch disparaît de l'écran
            finch.destroy()
            turtle.clearscreen() #l'écran redevient blanc
            
            ln= turtle.Screen() #création de la fenêtre
            ln.bgpic("fin.gif")
            #fermeture de l'écran
            turtle.ontimer(arret, 3000) # l'écran est fermé après 3 s
            
    #mettre à jour l'écran (screen)
    wn.update()
  
wn.exitonclick()#quitte si le bouton de la souris est cliqué
