import glob

# counts the number of files in a directory
countingfiles = input ("Type the directory you would like me to count the files in.")

counterfile = len(glob.glob(countingfiles))

print (counterfile)




# #find if a file exist within a directory
#
# user_input = input("Enter the path of your file: ")
#
# assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
# f = open(user_input,'r+')
# print("Hooray we found your file!")
# #stuff you do with the file goes here
# f.close()


# numberoffiles = input("What is the file path ? ")
#
#
# # simple version for working with CWD
# print (len([name for name in os.listdir('.') if os.path.isfile(name)])
#
# # path joining version for other paths
# dir = numberoffiles
#
# print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(dir, name))])
#
# except:
#     error = sys.exc_info()[0]
#     print ("I am sorry something went wrong")
#     print(error)
