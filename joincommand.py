ages =  open ("ages.txt", "r")
import csv

with open ("ages.txt", "r") as ages :
    listagesnames = csv.reader(ages)
    for currentRow in listagesnames :
        print(",".join(currentRow))
