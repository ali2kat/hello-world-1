import datetime
#
# currentdate



currentdate = datetime.date.today()
# currentTime = datetime.datetime.now()
# print(currentTime.minute)


print (currentdate)
print (currentdate.year)
print (currentdate.month)


# print (currentTime)
# print (currentTime.hour)
# print (currentTime.minute)
# print (currentTime.second)


print (currentdate.strftime('%d %b,%Y'))
print (currentdate.strftime('%d %b,%y'))


userInput = raw_input ("Please enter your birthday (mm/dd/yyyy)")
birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y' ).date()
print (birthday)

days = currentdate - birthday
print(days.days)
