#list of attendees
partyList = []
guests = ""

##adding names to a list and sorting it alphabetically code below.

while guests != "guests":
    guests = input ("Please type STOP when you are done ""\n"
"What is the name of the guests attending the party? ")
    partyList.append (guests)
    if guests == "STOP" :
        del partyList[-1]
        guests=partyList.sort()
        print(",".join(partyList))
        break





# guests.split()
# # for guests in guests :
# print (partyList)
