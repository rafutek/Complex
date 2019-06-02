# import librairies necessaires
import numpy as np # lib pour les tableaux
import math # lib pour la racine carre


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




print("Welcome, \nthis program reads two files to create complex numbers, and display a graph\n")

readFiles_writeMagZ()
