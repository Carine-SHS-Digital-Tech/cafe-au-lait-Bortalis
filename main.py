# setting starting variables
total = charge = go = end = 0
# prices
coffees = {"Cappuccino": 3, "Espresso": 2.25, "Latte": 2.5, "Iced Coffee": 2.5}
# print and input helper
lis = ["Cappuccino", "Espresso", "Latte", "Iced Coffee"]
# order storage
types = {"Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0}
# summery storage
total_summery = {"Dine": 0, "Take": 0, "Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0, "GST": 0, "Profit": 0, "Cups": 0, "Orders": 0}
# start and ending loop
while end == 0:
    # start valid value to "correct at the moment"
    valid = 1
    # first choice
    choice = input("\n\n______________________________________\nSo what do you want to do? \n1:New order   2:Daily summery    3:No\n\n")
    if choice.upper() in ["NEW ORDER", "1"]:
        if valid == 1:
            # resetting order values
            types = {"Cappuccino": 0, "Espresso": 0, "Latte": 0, "Iced Coffee": 0}
            total = go = 0
            # second choice
            dot = input("\n1:Dine in   2:Take away\n\n")
            if dot.upper() in ["DINE IN", "1"]:
                charge = 0
                total_summery["Dine"] += 1
                go = 1
            elif dot.upper() in ["TAKE AWAY", "2"]:
                charge = 1
                total_summery["Take"] += 1
                go = 1
            else:
                valid = 0
        # loop of the ordering of the actual items
        while go == 1:
            if valid == 1:
                choice = input("\nWhat drink do you want?\n1:Cappuccino $3.00\n2:Espresso $2.25\n3:Latte $2.50\n4:Iced Coffee $2.50\n\n")
                num = input("\nWhat quantity do you want of this drink?\n\n")
                if num.isnumeric() is True:
                    num = float(num)
                    num = int(round(num, 0))
                    if num < 0:
                        valid = 0
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
                            valid = 0
                else:
                    valid = 0
                # asking if they want to spend more
                if valid == 1:
                    answer = input("\nAnything else?\n 1:Yes   2:No\n\n")
                    if answer.upper() in ["YES", "1"]:
                        go = 1
                    else:
                        go = 0
                else:
                    go = 0
            else:
                go = 0
        if valid == 1:
            # finally working out the final price or the order
            for a in types:
                total += types[a]*coffees[a]
            if charge == 1:
                total = total*1.05
            gst = total*.1
            print(" ")
            # printing receipt
            for a in lis:
                print(f"{a}s:{types[a]}")
            print(f"\nInitial cost: ${total:.2f}")
            print(f"Gst cost: ${gst:.2f}")
            print(f"Final cost: ${(gst+total):.2f}")
            pay = input("\nPlease provide your payment in EXACT. Or larger if you feel like tipping.\n\n")
            if pay >= f"{(gst+total):.2f}":
                print("\nThank you for your order")
                for a in types:
                    total_summery[a] += types[a]
                    total_summery["Cups"] += types[a]
                total_summery["GST"] += int(round(gst, 0))
                total_summery["Profit"] += int(pay) - gst
                total_summery["Orders"] += 1
            else:
                print("\nPayment not correct, please restart order")
                valid = 0
        # failed validation statement
        if valid == 0:
            print("\nINCORRECT VALUE(S). PLEASE RESTART ORDER.")
    # simple summery
    elif choice.upper() in ["DAILY SUMMERY", "2"]:
        for a in total_summery:
            print(f"{a}:{total_summery[a]}")
    # code end condition
    elif choice.upper() in ["NO", "3"]:
        print("\nOh, ok...")
        end = 1
    else:
        print("\nINVALID INPUT")
print("Thank you for your participation!")
