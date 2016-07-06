import datetime

currentdatetime = datetime.date.today()
print (currentdatetime)
print (currentdatetime.year)
print (currentdatetime.month)
print (currentdatetime.day)


print (currentdatetime.strftime('%d %b,%Y'))
print (currentdatetime.strftime('%d %b,%y'))

print (currentdatetime.strftime \
	("Please attend my birthday %A, %B %d in the year %Y "))
