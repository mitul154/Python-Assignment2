"""
Assignment: Programming Strategies
A profit calculator for circle phones which calculates profit based on the period(day, week, weekend, weekday)

This calculator supports String and integer based inputs. And gives a string with the total profit as output
This calculator is designed to work in all scenario's
"""


#  defining variables

loopCondition = True
total = 0
product_category = 0
profit = [120.45, 99.50, 75.69, 65.73, 51.49]   # profits for products
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
no_of_days = {1:1, 2:7, 3:5, 4:2}   # dictionary representing number of days corresponding time_period values
period = {1:"", 2:"week", 3:"week (business days)", 4:"weekend"}
tp_loop = True      # Condition for the time period loop

print("Welcome to Circle Phones Profit calculator\n"
      "You can calculate the profit of the company according to a specific "
      "day or by a week or divide the week into weekdays and weekend\n")

# while loop which repeats itself if the entered value is incorrect

while tp_loop:
    time_period = input("Enter:\n"
                            "1 - For specific Day\n"
                            "2 - For the Week\n"
                            "3 - For Week Business Days\n"
                            "4 - For Weekend days\n"
                            "0 - Exit: ")
    if time_period.isnumeric(): # checks if time_period is an integer
        time_period = int(time_period)
    else:
        print("Invalid input, please enter a valid input")
        continue
    if 0 <= time_period <= 4:
        tp_loop = False
    else:
        print("Invalid input, please enter a valid input")
    if time_period == 0:
        quit()

# asking user for the specific day

if time_period == 1:
    while True:   # loop for entering specific day by the user
        day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: ")
        period[1] = day
        if day.casefold() not in days:
            print("Invalid input, please enter a valid input1")
        else:
            break
print("Select one of following product categories:\nCategory\tDescription\t\t\t\tAverage Profit Per Unit\n"
      "1\t\t\tApple iPhone	\t\t$120.45\n"
      "2\t\t\tAndroid Phone	\t\t$99.50 \n"
      "3\t\t\tApple Tablet	\t\t$75.69 \n"
      "4\t\t\tAndroid Tablet\t\t\t$65.73\n"
      "5\t\t\tWindows Tablet\t\t\t$51.49\n"
      )

for i in range(no_of_days[time_period]):    # repeats the code block as many times as number of days given
    if time_period == 4:
        print(f"For {days[i+5].capitalize()}")
    elif time_period == 1:
        print(f"For {day}")
    else:
        print(f"For {days[i].capitalize()}")

    while loopCondition:    # loop exits when user enters 0
          product_category = input("\nEnter product number 1-5, or enter 0 to stop: ")
          if product_category.isnumeric():  # checks if input is an integer
              product_category = int(product_category)
          else:
              print("Invalid input, please enter a valid input")
              continue
            # check for invalid input
          if product_category < 0 or product_category > 5:    # if the number is out of range the loop continues
                print("Error!!!, Enter a number between 0 and 5")
                continue

          if product_category == 0:
                break


          quantity = input("Enter quantity sold: ")
          if quantity.isnumeric():  # check if input is integer
              quantity = int(quantity)
          else:
                print("Error!!!, Enter a number between 0 and 5")
                continue

          total += profit[product_category - 1] * quantity  # calculates the total based on the given values


print(f"Total Profit for the {period[time_period]} is: ${total:.2f}")

if total >= 10000:
    print(f"You did good this {period[time_period]}! Keep up the great work!")
else:
    print(f"More hard work needed... The last {period[time_period]} wasn't the best")



