# starting variables
valid = 1
total = dine = take = charge = go = nice = end = 0
coffees = {"Cappuccino": 3, "Espresso": 2.25, "Latte": 2.5, "Iced Coffee": 2.5}
lis = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
types = {"Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0}
total_summery = {"Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0, "GST": 0, "Profit": 0, "Cups": 0, "Orders": 0}
while end == 0:
    valid = 1
    # and also this is the start of the program
    choice = input("\n\n______________________________________\nSo what do you want to do? \n1:New order   2:Daily summery    3:No\n\n")
    # this is here for when we take a new order
    if choice.upper() == "NEW ORDER":
        if valid == 1:
            types = {"Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0}
            dot = input("\n1:Dine in   2:Take away\n\n")
            if dot.upper() == "DINE IN":
                charge = 0
                dine += 1
                go = 1
            elif dot.upper() == "TAKE AWAY":
                charge = 1
                take += 1
                go = 1
            else:
                go = 1
                valid = 0
        if valid == 1:
            while go == 1:
                if valid == 1:
                    typeoh = input("\nWhat drink do you want?\n1:Cappuccino $3.00\n2:Espresso $2.25\n3:Latte $2.50\n4:Iced Coffee $2.50\n\n")
                    num = input("\nWhat quantity do you want of this drink?\n\n")
                    if num.isnumeric() is True:
                        num = float(num)
                        num = int(round(num, 0))
                        if num < 0:valid = 0
                        if valid == 1:
                            if typeoh.upper() == "CAPPUCCINO":types["Cappuccino"] += num
                            elif typeoh.upper() == "ESPRESSO":types["Espresso"] += num
                            elif typeoh.upper() == "LATTE":types["Latte"] += num
                            elif typeoh.upper() == "ICED COFFEE":types["Iced Coffee"] += num
                            else:valid = 0
                    else:valid = 0
                    if valid == 1:
                        answer = input("\nAnything else?\n 1:Yes   2:No\n\n")
                        if answer.upper() == "YES":go = 1
                        else:go = 0
                    else:go = 0
                else:go = 0
            if valid == 1:
                for a in types:total += types[a]*coffees[a]
                if charge == 1:total = total*1.05
                gst = total*.1
                print(" ")
                for a in lis:
                    print(f"{a}s:{types[a]}")
                print(f"\nInitial cost: ${total:.2f}")
                print(f"Gst cost: ${gst:.2f}")
                print(f"Final cost: ${(gst+total):.2f}")
                pay = input("\nPlease provide your payment in exact.\n\n")
                if pay == f"{(gst+total):.2f}":
                    print("\nThank you for your order")
                    for a in types:
                        total_summery[a] += types[a]
                        total_summery["Cups"] += types[a]
                    total_summery["GST"] += int(round(gst, 0))
                    total_summery["Profit"] += total
                    total_summery["Orders"] += 1
                else:
                    print("\nPayment not correct, please restart order")
                    valid = 0
        if valid == 0:print("\nINCORRECT VALUE(S). PLEASE RESTART ORDER.")
    elif choice.upper() == "DAILY SUMMERY":
        for a in total_summery:
            print(f"{a}:{total_summery[a]}")
    elif choice.upper() == "NO":
        print("\nOh, ok...")
        end = 1
        nice = 1
    else:print("\nINVALID INPUT")
if nice == 1:print("Thank you for your participation!")
