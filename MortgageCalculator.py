print ("THIS IA A LOAN CALCULATOR")


#declaring  and initalizing your veriables.
monthlypayment = 0
loanAmount = 0
interestrate = 0
numberofpayments = 0
loanDurationinYears = 0

#User information below
strloanAmount = input ("What is your loan amount?")
strinterestrate = input ("What is your interest you wish to pay?")
strloanDurationinYears = input ("How years will it take you to pay it")


loanAmount = float(strloanAmount)
interestrate = float(strinterestrate)
loanDurationinYears = float(strloanDurationinYears)

#one payment per month once *12
numberofpayments = loanDurationinYears*12


#Formula below for monthly payments.
monthlypayment = loanAmount * interestrate * (1 + interestrate) * numberofpayments / \
 ((1 + interestrate) * numberofpayments - 1)

print(monthlypayment)
