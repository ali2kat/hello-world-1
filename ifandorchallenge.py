#declaring veriables

country = ""
province = ""
orderTotal = 0
totalwithTax = 0


##declaring veriables to hold tax values used in the calculations
##That way if  a tax rate changes, I only have to change it in one place
##of searching through my code to see where I had a spacific value and updating it.

GST = .05
HST = .13
PST = .06

#Ask the user what country they are from
country = input("What country are you from?").upper()
#if they are from Canda ask the province... don't forget that may enter canada as
##CANADA, Candana, canada ,canada so convert the string to a case.

if country.upper() == "CANADA" :
    province = input("Which province are you from ? ")

#ask for the order total
orderTotal = float(input("what is your order total?"))

#now add the taxes
if country.upper() == "CANADA" :
    # if they are from canada, we have to change the calculation based on the province they specified
    if province.upper() == "alberta" :
        orderTotal = orderTotal + orderTotal * GST
    elif province.upper() == "ontario" or province.upper() ==  \
    "new brunswick" or province.upper() == "nova scotia" :
        orderTotal = orderTotal + orderTotal * HST
    else :
        orderTotal = orderTotal + orderTotal * PST + orderTotal * GST
# if they are not from canada  the is no tax, so the amount they entered is the total with tax
# and no modification to orderTotal is required.

#now display the total with taxer to the user, don;t forget to format the number
print("Your total including taxes come to $%.2f" % orderTotal)
