import tkinter as tk
import random


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

configuration(3)