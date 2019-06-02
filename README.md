# Complex

First of all, this code is in Frenglish, the program is in English and comments are in French.

I'll try to explain as clear as possible the aim of this code.

Here have a look at the beginning of a text file:
Temps 	Amplitude 
0   0
0	69.6193
1.84E-8	69.861
3.68E-8	70.2233
...

The first column is time, and the second is the value in function of that time.

This program can be explained as a menu:

1. Read ReZ.txt and ImZ.txt, compute and write MagZ (as MagZ = sqrt(ReZ + ImZ) ) into MagZ.txt.
2. Read one of the text files and display its graph


Now let's explain the functions in the program call order:
- First, global_menu() is called. This function displays the two choices as seen above, and returns the choice of the user.
- In the case where the user chose to read files, compute MagZ and write it iinto MagZ.txt, readFiles_writeMagZ() is called. This function gets the data written in the text files and save them into numpy arrays (one for each file), with time as first column, and the value corresponding in the second column.
If there is the same number of points in the two arrays, we can open MagZ.txt in write mode and write the colomn names.
Then, for each point of the arrays, we verify that the time is the same, compute the impedance ( MagZ = sqrt(ReZ + ImZ) ) and write the time and the result into MagZ.txt.
Finally we close the file.
- In the other case, where we have to read a file and display its graph, file_menu() is called to ask the user wich file we wants.
Then, if the choice is one of the text files, the program calls readFile_displayGraph(filename). This function gets the values and store them into a numpy array, the exact same way as done in readFiles_writeMagZ().
We choose that the first column is the abscissa, and the second the ordinate.
We give a name to the graph (the file name), and to coordinates with matplotlib functions. Finally we create and display the graph with other matplotlib functions.
