# from pygame import *

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLEU =  (  0,   0, 255)
GRIS = (128, 128, 128)
VIOLET = (98, 14, 104)
# Peut etre plus de couleurs ....

# Formes de Blocs : liste de coordonnees

carre = {'DOWN':[(6,19),(6,18),(7,19),(7,18)]}   # Jaune

laBarre = {'DOWN':[(5,19),(6,19),(7,19),(8,19)],
           'UP':[(7,18),(7,19),(7,20),(7,21)] } # Bleu

leThe = {'DOWN':[(5,19),(6,19),(7,19),(6,18)],   # Violet
          'UP':[(5,19),(6,19),(7,19),(6,18)]
}

eclaireD = [(6,19),(7,19),(5,18),(6,18)] # Vert
eclaireG = [(5,19),(6,19),(6,18),(7,18)] # Orange
elleD = [(5,19),(5,18),(6,18),(7,18)]  # Rouge
elleG = [(7,19),(5,18),(6,18),(7,18)]  # Rose


