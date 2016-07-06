animalFile = open("tasmania.txt","r")
import csv

# #read file line by line
#
# firstAnimal = animalFile.readline()
# print(firstAnimal)
# secondAnimal = animalFile.readline()
# print(secondAnimal)


with open("tasmania.txt","r") as animalFile :
    allRowsList = csv.reader(animalFile)
    for currentRow in allRowsList :
        print(",".join(currentRow))


        # for currentRow in currentRow :
        #     print (currentRow)
