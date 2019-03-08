import pygame as pyg
from CONST import *

class tablo:

    def __init__(self):
        self.tablo = [[0,0,0,0,0,0,0,0,0,0] for i in range(20)] # Indique presence des blocs
        self.score = 0
        
    
    # Actualise le tablo, les scores/combos
    def test(self):
        combo = 0
        for lignes in self.tablo:
            if not 0 in lignes:
                for j in range(i,19):
                    self.tablo[j] = self.tablo[j+1] # ca marche paa 
                self.score += int(x)
                combo += 1
                i -= 1

        if combo >= 4:
            self.score = int(x)
        # a continuer pour les combos et les scores

    def update(*positions): # update position du bloc + test si le bloc a fini de tomber      
        return




class newBlock:

    def __init__(self, forme):
        #donne une position de chaque bloc dans le tablo sous forme d'une liste de tuple = (x,y)
        # commence en (6,19)
        self.positions = [(0,0),(0,0),]   #givePositions(forme) + integrer dans tablo #Zach ou Brice
        self.forme = forme
        


    def deplacement(self,direction,tablo):
        if direction == 'BAS':
            peutDescendre = True
            for (x,y) in self.positions:
                if tablo[y-1][x]==0:
                    continue
                else:
                    peutDescendre = False
                    break
            if peutDescendre:
                tablo.update() # ajouter les arguments 
                for (x,y) in self.positions:
                    y -= 1
            
        elif direction == 'DROITE':
            for (x,y) in self.positions:
                if x<10 and tablo[y][x+1]==0:
                    continue
                else:
                    peutDroite = False
                    break
            if peutDroite:
                tablo.update() # ajouter les arguments
                for (x,y) in self.positions:
                    x += 1

        elif direction=='GAUCHE':
            for (x,y) in self.positions:
                if x>1 and tablo[y][x-1]==0:
                    continue
                else:
                    peutGauche = False
                    break
            if peutGauche:
                tablo.update() # ajouter les arguments
                for (x,y) in self.positions:
                    x -= 1 


    def rotation(forme):
        # test de possibilité de rotation i.e. repousse le bloc si y a pas la place
        pass

