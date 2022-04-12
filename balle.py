import tkinter as tk
from tracemalloc import stop

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
rebond_compte = 0


###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 30, 30
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")

    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    global rebond_compte
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 and rebond_compte !=30:
        balle[1] = -balle[1]
        rebond_compte = rebond_compte + 1
        print(rebond_compte)
        canvas.itemconfigure(balle[0], fill="blue")
    
    if x1 >= 600 and rebond_compte !=30:
        balle[1] = -balle[1]
        rebond_compte = rebond_compte + 1
        print(rebond_compte)
        canvas.itemconfigure(balle[0], fill="green")

        
    if y0 <= 0 and rebond_compte !=30:
        balle[2] = -balle[2]
        rebond_compte = rebond_compte + 1
        print(rebond_compte)
        canvas.itemconfigure(balle[0], fill="red")

    if y1 >= 400 and rebond_compte !=30:
        balle[2] = -balle[2]
        rebond_compte = rebond_compte + 1
        print(rebond_compte)
        canvas.itemconfigure(balle[0], fill="yellow")

    if rebond_compte == 30:
        balle[1] = 0
        balle[2] = 0
        


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

bord_gauche = canvas.create_rectangle((0,0),(5,400), fill = "blue")
bord_droit = canvas.create_rectangle((600,0),(595,400), fill = "green")
bord_haut = canvas.create_rectangle((0,0),(600,5), fill = "red")
bord_bas = canvas.create_rectangle((0,400),(600,395), fill = "yellow")





# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
