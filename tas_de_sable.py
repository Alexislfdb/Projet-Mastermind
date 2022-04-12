from re import A
import tkinter as tk
import random
from tracemalloc import stop


def configuration(n):
    ligne_configuration = []
    configuration_matrice = []
    for i in range(n):
        for j in range(n):
            ligne_configuration.append(random.randint(0,9))
        configuration_matrice.append(ligne_configuration)
        ligne_configuration = []
    for a in range(len(configuration_matrice)):
        print(configuration_matrice[a], "\n")
    
    return configuration_matrice



def interface():
    configuration_matrice_interface = configuration(3)

    def generer():
        racine.destroy()
        interface()

    

    x1, y1 = 50, 50
    x2, y2 = 300, 300
    x3, y3 = 350, 350
    x4, y4 = 600, 600
    x5, y5 = 650, 650
    x6, y6 = 900, 900

    racine = tk.Tk()
    canvas = tk.Canvas(racine, bg="black", width=950, height=950)
    bouton1 = tk.Button(racine, text="Génerer",command=generer)
    bouton2 = tk.Button(racine, text="Stabiliser")

    racine.title("Tas De Sable")


    canvas.grid()
    bouton1.grid(row=1)
    bouton2.grid(row=2)

    Carré1 = canvas.create_rectangle((x1, y1), (x2, y2), fill="white")
    Chiffre1 = canvas.create_text(175, 175, text=configuration_matrice_interface[0][0], font=("helvetica", "50", "bold"))

    Carré2 = canvas.create_rectangle((x1, y3), (x2, y4), fill="white")
    Chiffre2 = canvas.create_text(175, 475, text=configuration_matrice_interface[0][1], font=("helvetica", "50", "bold"))

    Carré3 = canvas.create_rectangle((x1, y5), (x2, y6), fill="white")
    Chiffre3 = canvas.create_text(175, 775, text=configuration_matrice_interface[0][2], font=("helvetica", "50", "bold"))

    Carré4 = canvas.create_rectangle((x3, y1), (x4, y2), fill="white")
    Chiffre4 = canvas.create_text(475, 175, text=configuration_matrice_interface[1][0], font=("helvetica", "50", "bold"))

    Carré5 = canvas.create_rectangle((x3, y3), (x4, y4), fill="white")
    Chiffre5 = canvas.create_text(475, 475, text=configuration_matrice_interface[1][1], font=("helvetica", "50", "bold"))

    Carré6 = canvas.create_rectangle((x3, y5), (x4, y6), fill="white")
    Chiffre6 = canvas.create_text(475, 775, text=configuration_matrice_interface[1][2], font=("helvetica", "50", "bold"))

    Carré7 = canvas.create_rectangle((x5, y1), (x6, y2), fill="white")
    Chiffre7 = canvas.create_text(775, 175, text=configuration_matrice_interface[2][0], font=("helvetica", "50", "bold"))

    Carré8 = canvas.create_rectangle((x5, y3), (x6, y4), fill="white")
    Chiffre8 = canvas.create_text(775, 475, text=configuration_matrice_interface[2][1], font=("helvetica", "50", "bold"))

    Carré9 = canvas.create_rectangle((x5, y5), (x6, y6), fill="white")
    Chiffre9 = canvas.create_text(775, 775, text=configuration_matrice_interface[2][2], font=("helvetica", "50", "bold"))

    racine.mainloop()

interface()



