print("Welcome to the tip calculator!")

# Getting the total bill and tip
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))

# Finding the percentage of tip and adding it to the bill
tip_percentage = tip/100
total_tip = bill * tip_percentage
total_bill = bill + total_tip

# Getting the number of people to split the bill
bill_split = int(input("How many people to split the bill? "))

# Finding the amount each person should pay and rounding it to 2 decimal places
each_person_bill = round(total_bill / bill_split,2)

# Printing the amount each person should pay
print(f"Each person should pay: ${each_person_bill}")