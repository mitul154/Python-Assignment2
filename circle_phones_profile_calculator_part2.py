while True:
    print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
    time_peroid = int(input("Enter:\n 1 - For specific Day\n 2 - For the Week \n 3 - For Week Business Days \n 4 - For Weekend days\n 0 - Exit\n "))

    weekly_set =[]

    if time_peroid == 1:
        weekly_set.append(str(input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday] \n")))
    elif time_peroid == 2:
        weekly_set = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]
    elif time_peroid == 3:
        weekly_set = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    elif time_peroid == 4:
        weekly_set = ["Saturday", "Sunday"]
    elif time_peroid == 0:
        print ("Program End!")
        break
    else:
        print("Invalid input, please enter a valid input")
        continue
    

    quantity_sold = int() 
    total = float()
    
    for i in weekly_set:
        print(f"for {i}")

        product_number = int(input("Enter product number 1-5, or enter 0 to stop:\n "))
    
    
        while True:
            if product_number < 0  or product_number > 5:
                print("Invalid Input, please enter a valid number")
                product_number = int(input("Enter product number 1-5, or enter 0 to stop: \n"))
            elif  0 < product_number <=5 :
                quantity_sold = int (input("Enter quantity sold:\n"))
                if product_number== 1:
                    total += 120.45 * quantity_sold
                elif product_number ==2:
                    total += 99.50 * quantity_sold
                elif product_number == 3:
                    total += 75.69 * quantity_sold
                elif product_number == 4:
                    total += 65.73 * quantity_sold
                elif product_number == 5:
                    total += 51.49 * quantity_sold
                else:
                    total += 0
                product_number = int(input("Enter product number 1-5, or enter 0 to stop:\n"))
            else:
                break

    print(round(total,2))


