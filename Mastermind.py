

import tkinter as tk
import random
from venv import create
# On appelle la librairie tkinter

num_code = 0
code_secret = []
code_essaie = []
nombre_essaies_restant = 10
bonne_place = 0
bonne_couleur = 0

def Mastermind():
    racine = tk.Tk()
    racine.title("Mastermind")
    bouton1 = tk.Button(racine, text="Partie 1 Joueur contre l'ordinateur", command=Partie_Un_Joueur)
    bouton2 = tk.Button(racine, text="Partie 2 Joueurs", command=Partie_Deux_Joueurs)
    bouton1.grid(row=1)
    bouton2.grid(row=2)
    racine.mainloop()

def Partie_Un_Joueur():

    racine = tk.Tk()
    racine.title("Mastermind")
    canvas = tk.Canvas(racine, bg="black", width=1600, height=900)
    canvas.grid()

    Code_Secret = []
    for i in range(4):
        code_secret.append(random.randint(1,8)) # Génération d'un code aléatoire

    

    rouge = canvas.create_oval((1200,100),(1250,150), fill="red")
    jaune = canvas.create_oval((1100,100),(1150,150), fill="yellow")
    blue = canvas.create_oval((1000,100),(1050,150), fill="blue")
    cyan = canvas.create_oval((1300,100),(1350,150), fill="cyan")
    violet = canvas.create_oval((1000,200),(1050,250), fill="purple")
    vert = canvas.create_oval((1100,200),(1150,250), fill="green")
    blanc = canvas.create_oval((1200,200),(1250,250), fill="white")
    orange = canvas.create_oval((1300,200),(1350,250), fill="#ff7f00")

    text_indice_place = canvas.create_text(1200, 400, text=("Veux dire qu'un pion est à la bonne place"), font=("helvetica", "15", "bold"),fill="white")
    canvas.create_oval((950,390),(970,410), fill="red")
    text_indice_couleur = canvas.create_text(1200, 500, text=("Veux dire qu'un pion est de la bonne couleur mais pas à la bonne place"), font=("helvetica", "15", "bold"),fill="white")
    canvas.create_oval((820,490),(840,510), fill="white")
    text_nombre_essaies = canvas.create_text(1200, 300, text=("Nombre d'essaies restants", nombre_essaies_restant), font=("helvetica", "15", "bold"),fill="white")
    text_choix = canvas.create_text(1200, 50, text=("L'ordinateur à générer un code aléatoire... Arriverez vous a le battre ?"), font=("helvetica", "15", "bold"),fill="white")
    canvas.create_text(1480,880,text="Retour en arrière", font=("helvetica", "20", "bold"), fill="white")
    

    def gestion_clic_2(coordonnees):
        global num_code, nombre_essaies_restant, code_essaie, bonne_couleur, bonne_place
        temp = 0
        temp2 = []
        

        
        if 1200 < coordonnees.x <1250 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="red")
            num_code = num_code + 1
            code_essaie.append(1)
        if 1100 < coordonnees.x <1150 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="yellow")
            num_code = num_code + 1
            code_essaie.append(2)
        if 1000 < coordonnees.x <1050 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="blue")
            num_code = num_code + 1
            code_essaie.append(3)
        if 1300 < coordonnees.x <1350 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="cyan")
            num_code = num_code + 1
            code_essaie.append(4)
        if 1200 < coordonnees.x <1250 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="white")
            num_code = num_code + 1
            code_essaie.append(5)
        if 1000 < coordonnees.x <1050 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="purple")
            num_code = num_code + 1
            code_essaie.append(6)
        if 1300 < coordonnees.x <1350 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="#ff7f00")
            num_code = num_code + 1
            code_essaie.append(7)
        if 1100 < coordonnees.x <1150 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="green")
            num_code = num_code + 1
            code_essaie.append(8)
        
        

        if num_code == 4:
            code_temp = code_secret
            for i in range(4):
                if code_essaie[i] == code_temp[i]:
                    temp2.append(code_essaie[i])
                    bonne_place = bonne_place + 1
            for i in range(4):
                if code_essaie[i] not in temp2:
                    if code_essaie[i] in code_temp:
                        for t in range(4):
                            if code_temp[i] == code_essaie[i]:
                                code_temp[i] = 9 
                        bonne_couleur = bonne_couleur + 1
            if bonne_place == 4:
                canvas.create_text(1200, 650, text=("Félicitation !"), font=("helvetica", "80", "bold"),fill="white")
                canvas.create_text(1200, 750, text=("Le décodeur à trouvé le code !"), font=("helvetica", "40", "bold"),fill="white")
                canvas.unbind("<Button-1>")

        

                
            print(bonne_couleur, bonne_place)

            while bonne_place > 0:
                temp = temp + 1
                canvas.create_oval((350+(temp*20),30+((10 - nombre_essaies_restant)*80)),(360+(temp*20),40+((10 - nombre_essaies_restant)*80)), fill="red")
                bonne_place = bonne_place - 1

            while bonne_couleur > 0:
                temp = temp + 1
                canvas.create_oval((350+(temp*20),30+((10 - nombre_essaies_restant)*80)),(360+(temp*20),40+((10 - nombre_essaies_restant)*80)), fill="white")
                bonne_couleur = bonne_couleur - 1
            
            num_code = 0
            nombre_essaies_restant = nombre_essaies_restant - 1
            canvas.itemconfig(text_nombre_essaies, text=("Nombre d'essaies restants", nombre_essaies_restant), state="normal")
            code_essaie = []
            if nombre_essaies_restant <= 0:
                canvas.create_text(1200, 650, text=("Dommage..."), font=("helvetica", "80", "bold"),fill="white")
                canvas.create_text(1200, 750, text=("L'ordinateur à gagné '!"), font=("helvetica", "40", "bold"),fill="white")
                canvas.unbind("<Button-1>")
                canvas.create_text(750, 175, text=("Le code secret était :"), font=("helvetica", "15", "bold"),fill="white")
                for i in range(4):
                    if code_secret[i] == 1:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="red")
                    if code_secret[i] == 2:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="yellow")
                    if code_secret[i] == 3:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="blue")
                    if code_secret[i] == 4:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="cyan")
                    if code_secret[i] == 5:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="white")
                    if code_secret[i] == 6:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="purple")
                    if code_secret[i] == 7:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="orange")
                    if code_secret[i] == 8:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="green")
                        
            
    canvas.bind("<Button-1>", gestion_clic_2)




def Partie_Deux_Joueurs():
    racine = tk.Tk()
    racine.title("Mastermind")
    canvas = tk.Canvas(racine, bg="black", width=1600, height=900)
    canvas.grid()

    text_choix = canvas.create_text(1200, 50, text=("Le premier joueur crée un code à 4 couleurs \n en cliquant sur les couleurs qu'il veut ajouter :"), font=("helvetica", "15", "bold"),fill="white")
    text_code_secret = canvas.create_text(275, 375, text=("Code secret choisis :"), font=("helvetica", "15", "bold"),fill="white")
    text_nombre_essaies = canvas.create_text(1200, 300, text=("Nombre d'essaies restants", nombre_essaies_restant), font=("helvetica", "15", "bold"),fill="white", state="hidden")


    rouge = canvas.create_oval((1200,100),(1250,150), fill="red")
    jaune = canvas.create_oval((1100,100),(1150,150), fill="yellow")
    blue = canvas.create_oval((1000,100),(1050,150), fill="blue")
    cyan = canvas.create_oval((1300,100),(1350,150), fill="cyan")
    violet = canvas.create_oval((1000,200),(1050,250), fill="purple")
    vert = canvas.create_oval((1100,200),(1150,250), fill="green")
    blanc = canvas.create_oval((1200,200),(1250,250), fill="white")
    orange = canvas.create_oval((1300,200),(1350,250), fill="#ff7f00")

    
    def gestion_clic_1(coordonnees):
        global num_code, code_secret
        
        if 1200 < coordonnees.x <1250 and 100 < coordonnees.y <150:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="red")
            num_code = num_code + 1
            code_secret.append(1)
        if 1100 < coordonnees.x <1150 and 100 < coordonnees.y <150:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="yellow")
            num_code = num_code + 1
            code_secret.append(2)
        if 1000 < coordonnees.x <1050 and 100 < coordonnees.y <150:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="blue")
            num_code = num_code + 1
            code_secret.append(3)
        if 1300 < coordonnees.x <1350 and 100 < coordonnees.y <150:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="cyan")
            num_code = num_code + 1
            code_secret.append(4)
        if 1200 < coordonnees.x <1250 and 200 < coordonnees.y <250:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="white")
            num_code = num_code + 1
            code_secret.append(5)
        if 1000 < coordonnees.x <1050 and 200 < coordonnees.y <250:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="purple")
            num_code = num_code + 1
            code_secret.append(6)
        if 1300 < coordonnees.x <1350 and 200 < coordonnees.y <250:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="#ff7f00")
            num_code = num_code + 1
            code_secret.append(7)
        if 1100 < coordonnees.x <1150 and 200 < coordonnees.y <250:
            canvas.create_oval((100+(num_code*100),450),(150+(num_code*100),500), fill="green")
            num_code = num_code + 1
            code_secret.append(8)

        if num_code == 4:
            num_code = 0
            text_valider = canvas.create_text(1175, 500, text=("Valider mon code secret"), font=("helvetica", "15", "bold"),fill="white")

        if len(code_secret) > 4:
            code_secret.pop(0)
        
        if 1000 < coordonnees.x < 1300 and 450 < coordonnees.y < 600 and len(code_secret) == 4:
            num_code = fin_code_secret()

        print(code_secret)
        print(num_code)
    
    canvas.bind("<Button-1>", gestion_clic_1)

    def fin_code_secret():
        canvas.create_rectangle((90,400), (1400,600), fill="black")
        canvas.unbind("<Button-1>")
        canvas.itemconfig(text_choix, state="hidden")
        canvas.itemconfig(text_code_secret, state="hidden")
        tour_adverse()
        num_code = 0
        return num_code
    
    def gestion_clic_2(coordonnees):
        global num_code, nombre_essaies_restant, code_essaie, bonne_couleur, bonne_place
        temp = 0
        temp2 = []
        

        
        if 1200 < coordonnees.x <1250 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="red")
            num_code = num_code + 1
            code_essaie.append(1)
        if 1100 < coordonnees.x <1150 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="yellow")
            num_code = num_code + 1
            code_essaie.append(2)
        if 1000 < coordonnees.x <1050 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="blue")
            num_code = num_code + 1
            code_essaie.append(3)
        if 1300 < coordonnees.x <1350 and 100 < coordonnees.y <150:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="cyan")
            num_code = num_code + 1
            code_essaie.append(4)
        if 1200 < coordonnees.x <1250 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="white")
            num_code = num_code + 1
            code_essaie.append(5)
        if 1000 < coordonnees.x <1050 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="purple")
            num_code = num_code + 1
            code_essaie.append(6)
        if 1300 < coordonnees.x <1350 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="#ff7f00")
            num_code = num_code + 1
            code_essaie.append(7)
        if 1100 < coordonnees.x <1150 and 200 < coordonnees.y <250:
            canvas.create_oval((10+(num_code*80),10+((10 - nombre_essaies_restant)*80)),(60+(num_code*80),60+((10 - nombre_essaies_restant)*80)), fill="green")
            num_code = num_code + 1
            code_essaie.append(8)
        


        if num_code == 4:
            code_temp = code_secret
            for i in range(4):
                if code_essaie[i] == code_temp[i]:
                    temp2.append(code_essaie[i])
                    bonne_place = bonne_place + 1
            for i in range(4):
                if code_essaie[i] not in temp2:
                    if code_essaie[i] in code_temp:
                        for t in range(4):
                            if code_temp[i] == code_essaie[i]:
                                code_temp[i] = 9 
                        bonne_couleur = bonne_couleur + 1
            if bonne_place == 4:
                canvas.create_text(1200, 650, text=("Félicitation !"), font=("helvetica", "80", "bold"),fill="white")
                canvas.create_text(1200, 750, text=("Le décodeur à trouvé le code !"), font=("helvetica", "40", "bold"),fill="white")
                canvas.unbind("<Button-1>")

        

                
            print(bonne_couleur, bonne_place)

            while bonne_place > 0:
                temp = temp + 1
                canvas.create_oval((350+(temp*20),30+((10 - nombre_essaies_restant)*80)),(360+(temp*20),40+((10 - nombre_essaies_restant)*80)), fill="red")
                bonne_place = bonne_place - 1

            while bonne_couleur > 0:
                temp = temp + 1
                canvas.create_oval((350+(temp*20),30+((10 - nombre_essaies_restant)*80)),(360+(temp*20),40+((10 - nombre_essaies_restant)*80)), fill="white")
                bonne_couleur = bonne_couleur - 1
            
            num_code = 0
            nombre_essaies_restant = nombre_essaies_restant - 1
            canvas.itemconfig(text_nombre_essaies, text=("Nombre d'essaies restants", nombre_essaies_restant), state="normal")
            code_essaie = []
            if nombre_essaies_restant <= 0:
                canvas.create_text(1200, 650, text=("Dommage..."), font=("helvetica", "80", "bold"),fill="white")
                canvas.create_text(1200, 750, text=("Le codificateur à gagné !"), font=("helvetica", "40", "bold"),fill="white")
                canvas.unbind("<Button-1>")
                canvas.create_text(750, 175, text=("Le code secret était :"), font=("helvetica", "15", "bold"),fill="white")
                for i in range(4):
                    if code_secret[i] == 1:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="red")
                    if code_secret[i] == 2:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="yellow")
                    if code_secret[i] == 3:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="blue")
                    if code_secret[i] == 4:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="cyan")
                    if code_secret[i] == 5:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="white")
                    if code_secret[i] == 6:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="purple")
                    if code_secret[i] == 7:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="orange")
                    if code_secret[i] == 8:
                        canvas.create_oval((600+(i*100),250),(650+(i*100),300), fill="vert")
           
        print(code_essaie)
        print(num_code)

    def tour_adverse():
        text_adversaire = canvas.create_text(1200, 50, text=("Maintenant, c'est au tour de \nl'adversaire de deviner le code secret!"), font=("helvetica", "15", "bold"),fill="white")
        text_indice_place = canvas.create_text(1200, 400, text=("Veux dire qu'un pion est à la bonne place"), font=("helvetica", "15", "bold"),fill="white")
        canvas.create_oval((950,390),(970,410), fill="red")
        text_indice_couleur = canvas.create_text(1200, 500, text=("Veux dire qu'un pion est de la bonne couleur mais pas à la bonne place"), font=("helvetica", "15", "bold"),fill="white")
        canvas.create_oval((820,490),(840,510), fill="white")
        canvas.itemconfig(text_nombre_essaies, text=("Nombre d'essaies restants", nombre_essaies_restant), state="normal") 
        canvas.bind("<Button-1>", gestion_clic_2)
    



    racine.mainloop()

Mastermind()
