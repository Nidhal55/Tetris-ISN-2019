import pygame as pyg
import CONST

class tablo:

    def __init__(self):
        self.tablo = [[0,0,0,0,0,0,0,0,0,0] for i in range(20)] # Indique presence des blocs
        self.score = 0
        
    
    # Actualise le tablo, les scores/combos
    def test(self):
        combo = 0
        for i in range(len(self.tablo)): # remplacer len jailaflemmedecompter
            if not 0 in self.tablo[i]:
                for j in range(i,19):
                    self.tablo[j] = self.tablo[j+1] # ca marche paa 
                self.score += int(x)
                combo += 1
                i -= 1

        if combo >= 4:
            self.score = int(x)
        # a continuer pour les combos et les scores

    def update(self, positionsAvant, positionsApres): # update position du bloc + test si le bloc a fini de tomber      
        for (x,y) in positionsAvant:
            self.tablo[y][x] = 0
        for (x,y) in positionsApres:
            self.tablo[y][x] = 1 # + la couleur




class newBlock:

    def __init__(self, forme, tablo):
        #donne une position de chaque bloc dans le tablo sous forme d'une liste de tuple = (x,y)
        # commence en (6,19)
        self.positions = give_position(forme, tablo)
        self.forme = forme
        self.orient = 'DOWN'
        


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
                posAvant = self.positions
                for (x,y) in self.positions:
                    y -= 1
                tablo.update(posAvant, self.positions)     
            
        elif direction == 'DROITE':
            for (x,y) in self.positions:
                if x<10 and tablo[y][x+1]==0:
                    continue
                else:
                    peutDroite = False
                    break
            if peutDroite:
                posAvant = self.positions
                for (x,y) in self.positions:
                    x += 1
                tablo.update(posAvant, self.positions)

        elif direction=='GAUCHE':
            for (x,y) in self.positions:
                if x>1 and tablo[y][x-1]==0:
                    continue
                else:
                    peutGauche = False
                    break
            if peutGauche:
                posAvant = self.positions
                for (x,y) in self.positions:
                    x -= 1 
                tablo.update(posAvant, self.positions)


    def rotation(self, forme):
        # test de possibilité de rotation + update positions
        if forme=='laBarre':
            if self.orient=='DOWN':
                positionsTest = []
                for (x,y) in self.positions:
                    positionsTest.append((x,y))
                    


def give_position(forme, tablo):  # forme vient de CONST et tablo est le tablo utilisé
    for (x,y) in forme:
        tablo.tablo[y][x] = 1 # ajouter code couleur ...a definir
    return(forme)
    

    
        


