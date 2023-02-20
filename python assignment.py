loopCondition = True
total = 0
product_category = 0
prices = [120.45, 99.50, 75.69, 65.73, 51.49]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
no_of_days = {1:1, 2:7, 3:5, 4:2}
period = {1:"", 2:"week", 3:"week (business days)", 4:"weekend"}
tp_loop = True

print("Welcome to Circle Phones Profit calculator\n"
      "You can calculate the profit of the company according to a specific "
      "day or by a week or divide the week into weekdays and weekend\n")


while tp_loop:
    time_period = input("Enter:\n"
                            "1 - For specific Day\n"
                            "2 - For the Week\n"
                            "3 - For Week Business Days\n"
                            "4 - For Weekend days\n"
                            "0 - Exit: ")
    if time_period.isnumeric():
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

if time_period == 1:
    while True:
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



for i in range(no_of_days[time_period]):
    if time_period == 4:
        print(f"For {days[i+5].capitalize()}")
    elif time_period == 1:
        print(f"For {day}")
    else:
        print(f"For {days[i].capitalize()}")

    while loopCondition:
          product_category = input("\nEnter product number 1-5, or enter 0 to stop: ")
          if product_category.isnumeric():
              product_category = int(product_category)
          else:
              print("Invalid input, please enter a valid input")
              continue

          if 0 <= product_category <= 5:
                innerLoop = False
          else:
                print("Error!!!, Enter a number between 0 and 5")
                continue

          if product_category == 0:
                break


          quantity = input("Enter quantity sold: ")
          if quantity.isnumeric():
              quantity = int(quantity)
          else:
                print("Error!!!, Enter a number between 0 and 5")
                continue

          total += prices[product_category-1] * quantity


"""if time_period == 1:
    print(f"Total Profit for the {day} is: ${total:.2f}")
else:"""
print(f"Total Profit for the {period[time_period]} is: ${total:.2f}")
if total >= 10000:
    print(f"You did good this {period[time_period]}! Keep up the great work!")
else:
    print(f"More hard work needed... The last {period[time_period]} wasn't the best")

"""elif time_period == 2:
    print(f"Total Profit for the week is: ${total:.2f}")
elif time_period == 3:
    print(f"Total Profit for the week (business days) is: ${total:.2f}")
elif time_period == 4:
"""


