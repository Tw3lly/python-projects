#Welcome messages and user inputs

#Welcome message
print("Welcome to the print calculator!\n") 

#User input for total bill and makes the input a float type
bill = float(input("What was the total bill? $"))

#User input for tip percentage and makes the input a float type
tip = float(input("How much tip would you like to give 10, 12 or 15? "))

#User input for amount of people who should split the bill and makes the input a float type 
split = float(input("How many people should split the bill? ")) 

# Calculations

# Divides tip by 100 so we can use it to calculate the percentage of the total bill (ex makes 12 to 0.12)
tip_calculation = tip / 100 

# Calculates the tip amount by using the bill total and times it by the percentage (ex $150 + 0.12 = 18)
tip_percentage = bill * tip_calculation 

# Calculates the total amount by adding the tip and bill together and then dividing it by the number of people who will split the bill. (ex. (150 + 18) / 5 = 33.6)
total = (tip_percentage + bill) / split

# prints total in an f string, 2.f will allow us to always display 2 decimals on the total amount. 
print(f"Each person should pay ${total:.2f}")
