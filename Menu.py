import pygame


# BROUILLON §§§§§§§§§§§§§§§§§§§§§§§§§§

# Initialise pygame
pygame.init()

fond = pygame.display.set_mode()
 
class Boutton(object):
 
    police  = pygame.font
    boutton = 'quelquechose' 
    rect    = boutton.get_rect()
 
    def __init__(self,lettre,position):
 
        self.image = Boutton.boutton.copy()
        self.rect = Boutton.rect.copy()
        self.lettre = Boutton.police.render(lettre,True,(255,255,255))
        self.rect_lettre = lettre.get_rect(center=Boutton.rect.center)
        self.image.blit(self.lettre,self.rect_lettre)
        self.rect.topleft = position
        self.Pos = self.get_rect()


A = Boutton('A',(100,550))
fond.blit(A.image,A.rect)






Boutton.rect = pygame.draw.rect(Boutton.fond, (couleurViolet), (100,550,50,50))
Boutton.rend = Boutton.police.render("A",True,(255,255,255))
Boutton.rect = Boutton.rend.get_rect()
Boutton.fond.blit(Boutton.rend,(110,545))
pygame.display.update()


