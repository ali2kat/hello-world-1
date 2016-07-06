fileName="demo.txt"
#accessmode = "w"
APPEND = "a"
WRITE ="w"

data = input("Please enter file info")

file = open(fileName, mode = WRITE)
file.write(data)

#Writing to a file below
# file = open(fileName,accessmode)
# file.write("This is the file first line \n")
# file.write("This is the second line in a file.")


#writing file to a  CSV file below
# file = open(fileName,accessmode)
# file.write("Susan,29\n")
# file.write("Christopher,31")


file.close()
print("file written successfully")
