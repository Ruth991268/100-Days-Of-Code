MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

is_on = True
profit_amount = 0  # Fixed: renamed to avoid conflict


def total_money():
    print("Please insert coins.")
    total = 0  # local variable, resets every time
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    print(f"You have paid a total of ${total:.2f}")
    return total


while is_on:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user == "off":
        is_on = False

    elif user == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit_amount:.2f}")

    elif user in MENU:
        drink = MENU[user]
        ingredients = drink["ingredients"]
        cost = drink["cost"]

        # ✅ Check if resources are enough
        enough_resources = True
        for item in ingredients:
            if ingredients[item] > resources.get(item, 0):
                print(f"Sorry, there is not enough {item}.")
                enough_resources = False

        if enough_resources:
            print(f"The total cost is ${cost}")
            money_received = total_money()

            if money_received >= cost:
                change = round(money_received - cost, 2)
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
                profit_amount += cost

                # ✅ Deduct resources
                for item in ingredients:
                    resources[item] -= ingredients[item]

                print(f"Here is your {user}. Enjoy! ☕")
            else:
                print("Sorry, that's not enough money. Money refunded.")

    else:
        print("Invalid option. Please select espresso, latte, or cappuccino.")
