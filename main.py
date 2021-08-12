# starting variables
go = end = 0
coffees = {"Cappuccino": 3, "Espresso": 2.25, "Latte": 2.5, "Iced Coffee": 2.5}
lis = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
lis2 = ["GST", "Profit", "Cups", "Orders"]
types = {"Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0}
total_summery = {"Dine": 0, "Take": 0, "Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0, "GST": 0, "Profit": 0, "Cups": 0, "Orders": 0}
# start of prcess
while end == 0:
    # operation mode
    choice = input("\n\n______________________________________\nSo what do you want to do? \n1:New order   2:Daily summery    3:No\n\n")
    if choice.upper() in ["NEW ORDER", "1"]:
        # resetting order items
        types = {"Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0}
        total = charge = 0
        # surcharge choice
        while go == 0:
            dot = input("\n1:Dine in   2:Take away (+.5% surcharge)\n\n")
            if dot.upper() in ["DINE IN", "1"]:
                charge = 0
                total_summery["Dine"] += 1
                go = 1
            elif dot.upper() in ["TAKE AWAY", "2"]:
                charge = 1
                total_summery["Take"] += 1
                go = 1
            else:
                print("\nINVALID ANSWER, PLEASE INPUT A VALID INPUT.")
        # Order start
        while go == 1:
            valid = 1
            # drink and quantity
            choice = input("\nWhat drink do you want?\n1:Cappuccino $3.00\n2:Espresso $2.25\n3:Latte $2.50\n4:Iced Coffee $2.50\n\n")
            num = input("\nWhat quantity do you want of this drink?\n\n")
            if num.isnumeric() is True:
                num = float(num)
                num = int(round(num, 0))
                if num < 0:
                    print("\nINVALID ANSWER, PLEASE INPUT A VALID INPUT.")
                    valid = 0
            else:
                print("\nINVALID ANSWER, PLEASE INPUT A VALID INPUT.")
                valid = 0
            # adding drink along to order
            if valid == 1:
                if choice.upper() in ["CAPPUCCINO", "1"]:
                    types["Cappuccino"] += num
                elif choice.upper() in ["ESPRESSO", "2"]:
                    types["Espresso"] += num
                elif choice.upper() in ["LATTE", "3"]:
                    types["Latte"] += num
                elif choice.upper() in ["ICED COFFEE", "4"]:
                    types["Iced Coffee"] += num
                else:
                    print("\nINVALID ANSWER, PLEASE INPUT A VALID INPUT.")
                    valid = 0
            # add to order
            if valid == 1:
                answer = input("\nAnything else?\n 1:Yes   2:No\n\n")
                if answer.upper() in ["YES", "1"]:
                    go = 1
                else:
                    go = 0
        go = 1
        # reciept
        for a in types:
            total += types[a]*coffees[a]
        if charge == 1:
            total = total*1.05
        gst = total*.1
        print(" ")
        for a in lis:
            print(f"{a}s:{types[a]}")
        print(f"\nInitial cost: ${total:.2f}")
        print(f"Gst cost: ${gst:.2f}")
        print(f"Final cost: ${(gst+total):.2f}")
        # here's a problem i could not solve, if i remove the isnumeric, it can fail if text is input, however now decimal points don't work, please help :(
        while go == 1:
            # payment time
            pay = input("\nPlease provide your payment round above to the nearest dollar (sorry). Or larger if you feel like tipping.\n\n")
            if pay.isnumeric() is True:
                if float(pay) >= float(gst+total):
                    # adding to summery
                    print("\nThank you for your order")
                    for a in types:
                        total_summery[a] += types[a]
                        total_summery["Cups"] += types[a]
                    total_summery["GST"] += gst
                    total_summery["Profit"] += float(pay) - gst
                    total_summery["Orders"] += 1
                    go = 0
                elif float(pay) < (gst+total):
                    print("\nNot enough funds, please enter more.")
                else:
                    print("\nINVALID ANSWER, PLEASE INPUT A VALID INPUT.")
            else:
                print("\nINVALID ANSWER, PLEASE INPUT A VALID INPUT.")
    # summery just prints out dict
    elif choice.upper() in ["DAILY SUMMERY", "2"]:
        for a in lis:
            print(f"{a}:{total_summery[a]}")
        for a in lis2:
            print(f"{a}:{total_summery[a]:.2f}")
    # ending condition
    elif choice.upper() in ["NO", "3"]:
        print("\nOh, ok...")
        end = 1
    else:
        print("INVALID ANSWER, PLEASE INPUT A VALID INPUT.")
print("Thank you for your participation!")
