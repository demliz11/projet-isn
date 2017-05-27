# -*- coding: utf-8 -*-
# script Finch.py
#co-auteure: Demay Lise
#j'ai trouvé ce programme qsur le site du finch
# je l'ai modifié en changeant des fonctions de noms, en remplaçant et en coupant
#toute une partie du programme qui ne me servait à rien
import time
import finchconnection
#création d'une classe finch
class Finch():

    def __init__(self):
        self.connection = finchconnection.ThreadedFinchConnection()
        self.connection.open()
        
    def led(self, *args):
        """contrôler la led
        """
        if len(args) == 3:
            r, g, b = [int(x) % 256 for x in args]
        elif (len(args) == 1 and isinstance(args[0], str)):
            color = args[0].strip()
            if len(color) == 7 and color.startswith('#'):
                r = int(color[1:3], 16)
                g = int(color[3:5], 16)
                b = int(color[5:7], 16)
        else:
            return
        self.connection.send(b'O', [r, g, b])

    #définition d'une fonction obstacle
    def obstacle(self):
        self.connection.send(b'I')
        data = self.connection.receive()
        if data is not None:
            gauche = data[0] != 0
            droite = data[1] != 0
            return gauche, droite


    def convertir_acceleration(self, a):
        """convertir l'acceleration"""
        
        if a > 31:
            a -= 64
        return a * 1.6 / 32.0

    def acceleration(self):
        """ returner (x, y, z, taper, bouger).  x, y, et z, désignent l'accélération de
            -1.5 to 1.5.
            quand le finch est à l'horizontal, z est proche de 1, x, y proche de 0.
            quand finch est sur sa queue, y, z sont proches de 0, x de -1
            taper, bouger sont des valeurs boléennnes -- true si l'évènement est réalisé
        """
        
        self.connection.send(b'A')
        data = self.connection.receive()
        if data is not None:
            x = self.convertir_acceleration(data[1])
            y = self.convertir_acceleration(data[2])
            z = self.convertir_acceleration(data[3])
            taper = (data[4] & 0x20) != 0
            bouger = (data[4] & 0x80) != 0
            return (x, y, z, taper, bouger)

    def roues(self, gauche, droite):
        """ contrôle roue droite et roue gauche
        les valeurs vont de -1.0 (recul) à 1.0 (avance) 
        """
        
        dir_gauche = int(gauche < 0)
        dir_droite = int(droite < 0)
        gauche = min(abs(int(gauche * 255)), 255)
        droite = min(abs(int(droite * 255)), 255)
        self.connection.send(b'M', [dir_gauche, gauche, dir_droite, droite])

    def arret(self):
        """ couper tous les moteurs et la led """
        self.connection.send(b'X', [0])

    def close(self):
        self.connection.close()
