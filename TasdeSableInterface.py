from cgitb import text
import tkinter as tk

x1, y1 = 50, 50
x2, y2 = 300, 300
x3, y3 = 350, 350
x4, y4 = 600, 600
x5, y5 = 650, 650
x6, y6 = 900, 900

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=950, height=950)
bouton = tk.Button(racine, text="Génerer")

canvas.grid()
bouton.grid()

Carré1 = canvas.create_rectangle((x1, y1), (x2, y2), fill="white")
Chiffre1 = canvas.create_text(175, 175, text="1", font=("helvetica", "50", "bold"))

Carré2 = canvas.create_rectangle((x1, y3), (x2, y4), fill="white")
Chiffre2 = canvas.create_text(175, 475, text="2", font=("helvetica", "50", "bold"))

Carré3 = canvas.create_rectangle((x1, y5), (x2, y6), fill="white")
Chiffre3 = canvas.create_text(175, 775, text="3", font=("helvetica", "50", "bold"))

Carré4 = canvas.create_rectangle((x3, y1), (x4, y2), fill="white")
Chiffre4 = canvas.create_text(475, 175, text="4", font=("helvetica", "50", "bold"))

Carré5 = canvas.create_rectangle((x3, y3), (x4, y4), fill="white")
Chiffre5 = canvas.create_text(475, 475, text="5", font=("helvetica", "50", "bold"))

Carré6 = canvas.create_rectangle((x3, y5), (x4, y6), fill="white")
Chiffre6 = canvas.create_text(475, 775, text="6", font=("helvetica", "50", "bold"))

Carré7 = canvas.create_rectangle((x5, y1), (x6, y2), fill="white")
Chiffre7 = canvas.create_text(775, 175, text="7", font=("helvetica", "50", "bold"))

Carré8 = canvas.create_rectangle((x5, y3), (x6, y4), fill="white")
Chiffre8 = canvas.create_text(775, 475, text="8", font=("helvetica", "50", "bold"))

Carré9 = canvas.create_rectangle((x5, y5), (x6, y6), fill="white")
Chiffre9 = canvas.create_text(775, 775, text="9", font=("helvetica", "50", "bold"))

racine.mainloop()