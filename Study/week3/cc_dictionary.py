inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for snow_inches in inches_snow.values():
        total_inches = total_inches + snow_inches
    print("Total snowfall inches: ", total_inches)


print_total_snowfall(inches_snow)
while True:
    userInput = input(
        "How many inches of snow fell on Thursday? (Enter whole number without decimal number) ")
    if userInput.isnumeric():
        break
    else:
        print("Incorrect value")

inches_snow["Thursday"] = int(userInput)
print_total_snowfall(inches_snow)
