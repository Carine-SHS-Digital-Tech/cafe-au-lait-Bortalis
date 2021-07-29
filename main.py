cap = 0
esp = 0
lat = 0
ice = 0
total = 0
dine = 0
take = 0
coffees = {cap: 3, esp: 2.25, lat: 2.5, ice: 2.5}
types = {cap: 0, esp: 0, lat: 0, ice: 0}
#def getprice():
#   for a in types:
#        total+=a*coffees[a]
#    return
choice = input("So what do you whant to do? \n\n1:New order   2:Daily summery\n\n")
if choice.upper() == "NEW ORDER":
        dot = input("\n1:Dine in   2:Take away\n\n")
        if dot.upper() == "DINE IN":
            charge = 0
            dine += 1
        elif dot.upper() == "TAKE AWAY":
            charge = 1
            take += 1
        type = input("\nWhat drink do you want?\nCappucino $3.00\nEspresso $2.25\nLatte $2.50\nIced Coffee $2.50\n\n")
        num = int(input("\nWhat quantity do you want of this drink?\n\n"))
        if type.upper() == "CAPPUCINO":
            types[cap]+=1*num
        elif type.upper() == "ESPRESSO":
            types[esp]+=1*num
        elif type.upper() == "LATTE":
            types[lat]+=1*num
        elif type.upper() == "ICED COFFEE":
            types[ice]+=1*num
        for a in types:
            total+=types[a]*coffees[a]
print (total)
print (total*.1)
if charge = 1:
    print (total*1.1*.05)
    print (total*1.1*1.05)
else:
    print (total*)
