

############### STARTING DATA ###############

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


############### FUNCTION DEFINITIONS ###############


def print_report(resources):
    """3. Print report of all coffee machine resources"""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${resources['money']}")


def ask_order():
    """1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)"""
    order = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    # 1.a Check the user’s input to decide what to do next.
    if order == "espresso" or order == "latte" or order == "cappuccino":
        return order

    elif order == "report":
        return order
    elif order == "off":
        return order
    else:
        print("Invalid Input")


def check_and_brew(MENU, resources, order):
    """4.a When the user chooses a drink,
    the program should check if there are enough resources to make that drink."""
    # TODO: 4.d. Skip key if ingredient not needed.
    #  Maybe use a "for" loop?
    for ingredient in MENU[order]:
        if (MENU[order][ingredient]) > (resources[ingredient]):
            print(f"Sorry there is not enough {ingredient}.")

    # TODO: 3.c Check payment before deducting.
        else:
            # 5.a If there are sufficient resources to make the drink selected,
            # then the program should prompt the user to insert coins
            purchased = process_coins(MENU, order, profit)

            # 3.b Make the report reflect updated resources dictionary
            if purchased:
                resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU[order]['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']


def process_coins(MENU, order, profit):
    # TODO: 5. Process coins
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    payment = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    dollars = round(payment, 2)

    if dollars < MENU[order]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = dollars - MENU[order]['cost']
        profit += dollars

        print(f"Here is ${change} in change.")
        print(f"Here is your {order}. Enjoy!")
        return True


def coffee_machine():
    """1.b The prompt should show every time action has completed."""
    machine_running = True
    while machine_running:
        order = ask_order()

        if order not in MENU:
            if order == "report":
                print_report(resources)

            # 2. Turn off the Coffee Machine by entering “off” to the prompt.
            elif order == "off":
                print("Status: Shut Down")
                break
        else:
            purchased = False
            check_and_brew(MENU, resources, order)


############### PROGRAM PROPER ###############
coffee_machine()