import sys

firstNumber = float(input("Enter the first number "))
secondNumber = float(input("Enter a number "))
try:
    result = firstNumber / secondNumber
    print (result)
except:
    error = sys.exc_info()[0]
    print ("I am sorry something went wrong")
    print(error)
    sys.exit()
finally:
    print("I will always run :-)")
