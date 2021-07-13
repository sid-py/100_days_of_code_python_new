import random
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

run_coffee_machine = True
total_balance = 0
paid_amt = 0 
   
# TODO 5: Process coins
def pay_money():
    print("Please insert coins:")
    quarters = int(input("how many quarters?")) * 0.25
    dimes = int(input("how many dimes?")) * 0.1
    nickels = int(input("how many nickels?")) * 0.05
    pennies = int(input("how many pennies?")) * 0.01
    total_payment = quarters + dimes + nickels + pennies
    return total_payment
  
def deliver_coffee(coffee_type):
    global total_balance, paid_amt
    if coffee_type == "espresso":
        if MENU[coffee_type]["ingredients"]["water"]  <= resources["water"]:
            if MENU[coffee_type]["ingredients"]["coffee"]  <= resources["coffee"]:
                paid_amt = pay_money()
                # TODO 6: Check transaction successful?
                if paid_amt >= MENU[coffee_type]["cost"]:
                    print(f"""Here is ${paid_amt - MENU[coffee_type]["cost"]} in change.""")
                    # TODO 7: Make COffee
                    print(f"Here is your {coffee_type}.")
                    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
                    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
                    total_balance += paid_amt
                else:
                    print("Sorry thats not enough money. Money refunded.")
        else:
            print("Sorry, Coffee unavailable!")
            run_coffee_machine = False
                   
    elif coffee_type == "latte" or coffee_type == "cappuccino":
        if MENU[coffee_type]["ingredients"]["milk"] <= resources["milk"]:
            if MENU[coffee_type]["ingredients"]["water"]  <= resources["water"]:
                if MENU[coffee_type]["ingredients"]["coffee"]  <= resources["coffee"]:
                    paid_amt = pay_money()
                    # TODO 6: Check transaction successful?
                    if paid_amt >= MENU[coffee_type]["cost"]:
                        print(f"""Here is ${paid_amt - MENU[coffee_type]["cost"]} in change.""")
                        # TODO 7: Make COffee
                        print(f"Here is your {coffee_type}.")
                        resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
                        resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
                        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
                        total_balance += paid_amt
                    else:
                        print("Sorry thats not enough money. Money refunded.")
            else:
                print("Sorry, Coffee unavailable!")
                run_coffee_machine = False
    # TODO 3: Print Report
    elif coffee_type == "report":
        for k,v in resources.items():
            print(k,v) 
        print("Money: $",total_balance)

def refill_resources():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
        
# TODO #2 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while run_coffee_machine:
    user_command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    if user_command == "off":
        run_coffee_machine = False
        
    # TODO 4: Check resources sufficient?
    deliver_coffee(user_command)
    
    if user_command == "refill":
        refill_resources()




            

        
        
        

        
            
            
    
