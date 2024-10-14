from art import logo
from art import cup

print(f"\033[38;5;220m{logo}")
print(f"{cup}\033[0m")



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "long black": {
        "ingredients": {
            "water": 100,
            "coffee": 24,
        },
        "cost": 2.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# This variable is to count the money inserted into the machine money box.
profit = 0
# This variable indicates the resources that are inside the machine
resources = {
    "water": 500,
    "milk": 400,
    "coffee": 100,
}


# This function is to check if there are enough ingredients to complete the order of the user. So, we are going to loop through all the ingredients that are required for the user drink selection.
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient """
    is_enough = True
    # example:  if we fetch the value from order_ingredients with the key of water, we should get hold of 200
    for item in order_ingredients:
        # - We would now test to see if 200 is greater than or equal to the 300 that we have under the resources, well, in this case then we should probably tell the user that we actually can't make it.
        if order_ingredients[item] >= resources[item]:
            print(f"\033[38;5;196m -Sorry, there is not enough \033[0m{item} \033[38;5;196m in the machine. Please, contact the owner.\033[0m")
            print("\n" * 2)
            # -in this case, we're going to return False because there is not enough resources.
            is_enough = False
   # - but otherwise, if we managed to get to the end of the for loop and we still haven't returned or exited the function by returning False, then, in this case, we can return True.
    return is_enough


# Process Coins. This function is to return the total value of the coins inserted
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("PLEASE, INSERT COINS")
    print("\n")
    # AUD$
    total = int(input("-How many $2 coins?\033[38;5;2m\n")) * 2.00
    total += int(input("\033[38;5;255m-How many $1 coins?\033[38;5;2m\n")) * 1.00
    total += int(input("\033[38;5;255m-How many 50 cents coins?\033[38;5;2m\n")) * 0.50
    total += int(input("\033[38;5;255m-How many 20 cents?\033[38;5;2m\n")) * 0.20
    total += int(input("\033[38;5;255m-How many 10 cents coins?\033[38;5;2m\n")) * 0.10
    total += int(input("\033[38;5;255m-How many 5 cents coins?\033[38;5;2m\n")) * 0.05

    return total


# This function will check if the user inserted enough money for the drink that he selected
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient """
    if money_received >= drink_cost:
        # - This is for giving the change to user if they inserted more money than the cost of the drink
        change = round(money_received - drink_cost, 2)
        print("\n")
        print(f"\033[38;5;255m-Here is your change: \033[38;5;220m ${change}\033[0m")
        # -if this money_received is greater or equal to the drink_cost, then we're going to add to this variable called 'profit'
        # -So, we're going to add the 'drinks_cost' to 'profit'.
        global profit # you'll see an error under the profit because this is acting inside a local scope and profit is outside in the global scope. So, in order to reach it, we have to say global profit.
        profit += drink_cost
        return True
    else:
        # - ATTENTION: Remember that the return has to be the last thing in your function, if you put this above the print statement then the print statement will never get called.
        print("\n")
        print("\033[38;5;196m-Sorry, that's not enough. Money refunded.\033[0m")
        print("\n")
        return False

# This is the function that will make the coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients form the resources."""
    # - we're going to get hold of the order_ingredients, and we're going to loop through them.
    # - So for each of the item in the order_ingredients, we're going to look inside the 'resources' for that particular item,
    #   and we're going to subtract the amount that's in the order_ingredients.
    for item in order_ingredients:
            resources[item] -= order_ingredients[item]
    print("\n")
    print(f"\033[38;5;255m-Here is your {drink_name}☕. Enjoy!")
    print("\n" * 3) 


# variable to exit the while loop for starting the machine. In this case let's say that is the power button
is_on = True

# Here we start the program
while is_on:
    print("\033[38;5;255mG'DAY MATE!")
    print("\n")
    print("PRICES:")
    print("\033[38;5;221mEspresso\033[0m \033[38;5;255m→ AU$1.50")
    print("\033[38;5;221mLong Black\033[0m \033[38;5;255m→ AU$2.00")
    print("\033[38;5;221mLatte\033[0m \033[38;5;255m→ AU$2.50")
    print("\033[38;5;221mCapuccino\033[0m \033[38;5;255m→ AU$3.00") 
    print("\n")
    # variable that holds the user choice
    print("\033[38;5;255m-What would you like to order?")
    print("\n")
    choice = input("-Type: | \033[38;5;221mEspresso\033[0m \033[38;5;255m| \033[38;5;221mLong Black\033[0m \033[38;5;255m| \033[38;5;221mLatte\033[0m \033[38;5;255m| \033[38;5;221mCappuccino\033[0m \033[38;5;255m|\n").lower()
    print("\n")
    # if else statements for making a Menu for controlling the machine. This would only apply for the owner of the machine.
        # - Stop the while loop which means to turn off the machine with a secret word in this case will be 'off'
    if choice == "off":
        print("The Machine is now \033[38;5;196mOFF\033[0m")
        print("\n")
        is_on = False
        # - Secret word to access the machine statistics set to 'report'
    elif choice == "report":
        # - Variable is 'resources' and we are aiming to key 'water' <-["water"] inside this 'resources' variable
        print("\n")
        print("\033[38;5;220mSTATISTICS:")
        print(f"Water left: {resources['water']}ml")
        print(f"Milk left: {resources['milk']}ml")
        print(f"Coffee left: {resources['coffee']}g")
        print(f"Money: ${profit}\033[0m")
        print("\n")
        # - If 'off' or 'report' is no typed then probably the user is entering a drink. So, this part applies for the regular user.
    else:
        # - We are creating a variable named 'drink' that catches a drink from the variable 'MENU' and aims to the one that the user inserted as input on 'choice' variable.
        drink = MENU[choice]
        # here we are calling the function that checks the amount of ingredients left. In order to do that the 'order_ingredients' will be from the drink and then getting hold of the values under the key 'ingredients' from 'MENU' variable
        if is_resource_sufficient(drink["ingredients"]):
            # - If there is enough resources to make the drink the next step is to ask for the payment.
            payment = process_coins()
            """here we call 'is_transaction_successful', and we're going to pass in the 'money_received' and the 'drink_cost'.
                So, the 'money_received' is going to be the 'payment' from the previous step that was calculated
                from all the coins,and the 'drink_cost' is going to be based on the drink,
                and it's under the key, "cost", which is in the 'MENU' variable."""
            if is_transaction_successful(payment, drink["cost"]):
                """If the transaction is successful and there are enough resources to make the drink,
                then the ingredients to make the drink should be deducted from the
                coffee machine resources """
                # - We need to give the drink_name, which is going to be the choice that the user entered, and the order_ingredients, which is going to come from the drink, and it's under the key, "ingredients" from MENU variable.
                make_coffee(choice, drink["ingredients"])








