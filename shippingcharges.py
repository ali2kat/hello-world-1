
tax = 10

totalpurchase = int(input("How much is your item?"))
if totalpurchase >= 49 :
    print ("there will be no additional charge")
    print ("$"+str(totalpurchase))
else:
    print  ("there will be additional $10 charges in heavy tax's.")
    print ("$"+str(totalpurchase + tax))
