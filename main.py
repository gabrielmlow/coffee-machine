MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

net_profit = 0


# TODO Print Report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")


# TODO Check Resources
def check_resource(choice):
    i = 0
    sufficient = True

    # collect choice ingredients
    ingredient = MENU[choice]["ingredients"]
    ingredients = [ingredient["water"], ingredient["milk"], ingredient["coffee"]]

    # collect the available resource
    available = [resources["water"], resources["milk"], resources["coffee"]]

    # compare
    while sufficient and i < len(ingredients):
        if (available[i] - ingredients[i]) < 0:
            sufficient = False
            print("Coffee Unavailable, Please Select Another Option")
            on_start()
        else:
            i += 1


# TODO Insert Coins
def insert_coins():
    total = 0.00

    print("Please insert coins.")
    total += (float(input("how many quarters? ")) * .25)
    total += (float(input("how many dime? ")) * .1)
    total += (float(input("how many nickel? ")) * .05)
    total += (float(input("how many penny? ")) * .01)

    return total


# TODO Validate Amount
def validate_amount(cost, received):
    # compare the prices
    # if the received is smaller, then reject
    if received < cost:
        print("Transaction Cancelled: Insufficient Amount")
        on_start()

    # if the received is exact
    elif received == cost:
        return True

    # if the received is more
    elif received >= cost:
        # give change
        change = float(received - cost)
        print("Here is your change: $" + str(change))
        # give coffee
        return True

    else:
        print("Unknown Error")
        on_start()


# TODO Update Resource
def update_resource(choice):
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]


# TODO Controller
def on_start():
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        cost = MENU[choice]["cost"]

        # check resource
        check_resource(choice)

        # insert coins
        received = insert_coins()

        # validate amount
        validate_amount(cost, received)

        # give coffee
        print(f"Here is your {choice}, enjoy :)")

        # add to net_profit
        global net_profit
        net_profit += cost

        # recalculate resource
        update_resource(choice)

        # restart program
        on_start()

    elif choice == "report":
        print_report()
        on_start()

    else:
        print("Try again!")
        on_start()


# TODO Initialization
on_start()