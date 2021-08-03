valid = 1
nice = 0
def neworder():
    #setting order variables
    cap = esp = lat = ice = total = dine = take = charge = go = 0
    coffees = {cap: 3, esp: 2.25, lat: 2.5, ice: 2.5}
    lis = [cap, esp, lat, ice]
    types = {cap: 0, esp: 0, lat: 0, ice: 0}
    valid = 1

    if valid == 1:
        dot = input("\n1:Dine in   2:Take away\n\n")
        if dot.upper() == "DINE IN" or "1":
            charge = 0
            dine += 1
            go = 1
        elif dot.upper() == "TAKE AWAY" or "2":
            charge = 1
            take += 1
            go = 1
        else:
            go = 1
            valid = 0

    if valid == 1:
        while go == 1:
            if valid == 1:
                type = input("\nWhat drink do you want?\nCappucino $3.00\nEspresso $2.25\nLatte $2.50\nIced Coffee $2.50\n\n")
                num = int(input("\nWhat quantity do you want of this drink?\n\n"))

                if valid == 1:
                    if type.upper() == "CAPPUCINO":
                        types[cap] += num
                    elif type.upper() == "ESPRESSO":
                        types[esp] += num
                    elif type.upper() == "LATTE":
                        types[lat] += num
                    elif type.upper() == "ICED COFFEE":
                        types[ice] += num
                    else:valid = 0
                if valid == 1:
                    answer = input("\nAnything else?\n 1:Yes   2:No\n\n")
                    if answer.upper() == "YES":
                        go = 1
                    else:
                        go = 0
            else:
                go = 0

        if valid == 1:
            for a in types:
                total+=types[a]*coffees[a]

            if charge == 1:
                total = total*1.05
            gst = total*.1
            print(f"\nInital cost: ${total:.2f}")
            print(f"Gst cost: ${gst:.2f}")
            print(f"Final cost: ${(gst+total):.2f}")
            for a in lis:
                print(a, types[a])
            print("Thank you for your order")
    if valid == 0:
        print("INCORRECT VALUE. PLEASE RESTART ORDER.")

#this is here for when we take a new order
while valid == 1:
    #and also this is the start of the program
    choice = input("\n\n\nSo what do you want to do? \n1:New order   2:Daily summery    3:No\n\n")
    if choice.upper() == "NEW ORDER" or "1":
        neworder()
    elif choice.upper() == "DAILY SUMMERY" or "2":
        print("STILL IN PROGRESS")
    elif choice.upper() == "NO" or "3":
        print("\nOh, ok...")
        valid = 0
        nice = 1
    else:
        valid = 0


if nice == 1:
    print("Thank you for your participation!")
elif valid == 0:
    print("\nINVALID ANSWER, PLEASE RESTART ACTIONS.")

