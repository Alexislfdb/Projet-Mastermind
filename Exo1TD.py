Monfichier = open("notes", "r")

moyenne_liste = []
notes_liste = []

while True:
    ligne = Monfichier.readline()
    if ligne == "":
        break
    var = ligne.split()
    moyenne_var = (int(var[1])+int(var[2])+int(var[3]))/3
    moyenne_liste.append(moyenne_var)
    notes_liste.append(ligne)


Monfichier.close()

Monfichier = open("Moyenne", "w")

for i in range(len(moyenne_liste)):
    Monfichier.write(notes_liste[i])
    Monfichier.write(str(moyenne_liste[i]))
    Monfichier.write("\n")

