# Coffee Machine Project
from data import MENU
from data import resources
from data import value_of_coins


def format_report():
    """Formats a report and returns it."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    coins = resources["coin"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nCoins: ${coins}"


def check_resources(choice, resources, menu):
    """Checks if there is enough resources for a customers order"""
    if choice == "espresso" and resources["water"] >= 50 and resources["coffee"] >= 18:
        return 1
    elif choice == "latte" and resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
        return 1
    elif choice == "cappuccino" and resources["water"] >= 250 and resources["milk"] >= 100 and resources[
         "coffee"] >= 24:
        return 1
    else:
        return 0


def coin_checker(value_of_c, total_amount, cost_of_coffee):
    """Prompts user to insert money, checks if it's enough and returns change"""
    for k, c in value_of_coins.items():
        amount_of_coins = int(input(f"How many {k}s ${c}?: "))
        total_amount += c * amount_of_coins
        # print(total_amount)
    if total_amount >= cost_of_coffee:
        change_returned = round(total_amount - cost_of_coffee, 2)
        print(f"Here is ${change_returned} in change")
        return 1
    else:
        return 0


def adjust_resources(order_ingredients, choice):
    """Adjusts resources in the dictionaries"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    resources["coin"] += choice["cost"]


total_coins = 0

is_machine_off = False
while not is_machine_off:
    user_choice = input("What would you like? (espresso $1.5/latte $2.5/cappuccino $3): ").lower()
    # If user choice is OFF machine will turn off and end the program.
    if user_choice == "off":
        is_machine_off = True
    # If user choice is report, it will call the format_report function and print the report.
    elif user_choice == "report":
        print(f"{format_report()}")
    else:
        # If user chose one of the drinks and there is enough resources, it will prompt user for payment.
        if check_resources(user_choice, resources, MENU) == 1:
            drink = MENU[user_choice]
            # Processes payment
            if coin_checker(value_of_coins, total_coins, cost_of_coffee=MENU[user_choice]['cost']) == 1:
                # Adjusts resources if payment was successful.
                adjust_resources(drink["ingredients"], MENU[user_choice])
                print(f"Here is your {user_choice}!")
            else:
                # If payment was unsuccessful user will be prompted and loop will start over.
                print("Sorry, that's not enough money.")
        else:
            # If there is not enough resources, user will be prompted and loop will start over. 
            print("There's not enough resources.")
