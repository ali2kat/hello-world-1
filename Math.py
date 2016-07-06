area = 0
height = 10
width = 20
'''
the area of a triangle
'''
area = width * height /2


#printed float  value of .2  decimal
print ("The area of a triangle %.2f " % area)


print('My favorite number is %6d!' % 42 )
print('My favorite number is %06d!' % 42 )

# alternet way to space for formating.
print("I have {0:d} dogs.".format(6))
print("I have {0:3d} dogs.".format(6))
print("I have {0:6d} dogs.".format(6))


print("I have {0:f} dogs.".format(area))
print("I have {0:42d} dogs.".format(42))



###backslash tells string that the next line is the same string
print("I have three numbers! " + \
	"The first is {0:3d} The Second is {1:4d} and then the {2:5d}" .format(7,8,9))








