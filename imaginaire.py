# import librairies necessaires
import numpy as np # lib pour les tableaux
import math # lib pour la racine carre
from matplotlib import pyplot as plt # lib pour le graph

def global_menu():
    print("Welcome\n")
    choice ='0'
    while choice =='0':
        print("Choose 1 to compute MagZ from ReZ.txt and ImZ.txt, and write it into MagZ.txt")
        print("Choose 2 to create a graph from a file")

        choice = input ("Please make a choice: ")

        if choice == "1":
            print("Let's compute MagZ and create MagZ.txt\n")
        elif choice == "2":
            print("You want to create a graph from a file")
        else:
            print("I don't understand your choice.")
    
    return choice

def file_menu():
    print("You have to choose the file you want\n")
    choice ='0'
    while choice =='0':
        print("Choose 1 for ReZ.txt")
        print("Choose 2 for ImZ.txt")
        print("Choose 3 for MagZ.txt")

        choice = input ("Please make a choice: ")

        if choice == "1":
            print("Let's read ReZ.txt and display the graph\n")
            return "ReZ.txt"
        elif choice == "2":
            print("Let's read ImZ.txt and display the graph\n")
            return "ImZ.txt"
        elif choice == "3":
            print("Let's read MagZ.txt and display the graph\n")
            return "MagZ.txt"
        else:
            print("I don't understand your choice.")
            return '0'


def readFiles_writeMagZ():
    # recuperation des donnees des fichiers sous forme de tableaux
    dataRe = np.genfromtxt('./ReZ.txt',skip_header=2)
    dataIm = np.genfromtxt('./ImZ.txt',skip_header=2)

    if dataRe.shape == dataIm.shape: # verifie qu'il y a autant de reels que d'imaginaires
        print("same number of points in the two files,\nso let's compute MagZ and write into MagZ.txt")
        file = open("./MagZ.txt","w") 
        file.write("Temps   Amplitude\n\n")
        data = np.empty(dataRe.shape) # creation d'un tableau de la meme taille 
        for i in range(dataRe.shape[0]): # pour chaque ligne..
            if dataIm[i,0] == dataRe[i,0]: # ..on verifie que le temps est le meme et si c'est le cas..
                data[i,0] = dataRe[i,0] # ..on entre le temps..
                data[i,1] =  math.sqrt(dataRe[i,1] + dataIm[i,1]) # ..et magZ dans le nouveau tableau
                file.write( str(data[i,0]) + " "+  str(data[i,1]) + "\n\n")
                
        file.close()
    else:
        print("different number of points in the two files so program stoped")
        exit(1)


def readFile_displayGraph(filename):
    data = np.genfromtxt(filename,skip_header=2) # recupere le temps et l'amplitude du fichier sous forme de tableau 2D
    x = data[:,0] # l'abscisse correspond a la premiere colonne
    y = data[:,1] # et l'ordonnee a la deuxieme
    plt.title(filename) # on donne un titre au graph
    plt.xlabel("Temps") # on nomme les axes
    plt.ylabel("Amplitude") 
    plt.plot(x,y) # on cree le graph 
    plt.show() # et on l'affiche


# Le programme commence ici
choice = global_menu() # menu principal, creation MagZ.txt ou affichage courbe
if choice == "1":
    readFiles_writeMagZ()# lecture ReZ.txt et ImZ.txt, calcul de MagZ et ecriture dans MagZ.txt
elif choice == "2": # si affichage courbe on doit choisir le fichier
    filename = file_menu()
    if filename != '0':
        readFile_displayGraph(filename)# lecture du fichier en question et affichage de sa courbe