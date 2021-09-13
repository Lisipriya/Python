from resources import MENU, resources


def call_report():
    for item in resources:
        report[item] = resources[item]
    return report


def check_resources_sufficiency(report):
    for values in report:
        report_quantity = report[values]
        if MENU[choice]["ingredients"].__contains__(values):
            resource_quantity = MENU[choice]["ingredients"][values]
            if report_quantity < resource_quantity:
                return False, values
    return True, " "


def process_coins(choice):
    print("Please insert the coins")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    total_dollar_given = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return total_dollar_given


def check_transaction_sufficiency():
    rate_of_the_item = MENU[choice]["cost"]
    print(rate_of_the_item)
    print(customer_amount)
    money = 0
    if customer_amount < rate_of_the_item:
        return f"Sorry that's not enough money. Money refunded.", False, money
    elif customer_amount > rate_of_the_item:
        bill = round(customer_amount - rate_of_the_item, 2)
        money += rate_of_the_item
        return f"Here is ${bill} in change.\nHere is your {choice} ☕️.Enjoy!", True, money
    else:
        money += rate_of_the_item
        return f"Here is your {choice} ☕️.Enjoy!", True, money


def modified_report(resources):
    for values in resources:
        resource_quantity = resources[values]
        if MENU[choice]["ingredients"].__contains__(values):
            ingredients_quantity = MENU[choice]["ingredients"][values]
            final_quantity = resource_quantity - ingredients_quantity
            resources[values] = final_quantity


total_money = 0
machine_operation = True

while machine_operation:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    report = {}
    if choice == "report":
        report_resources = call_report()
        for items in report:
            if items == "coffee":
                print(f"{items.title()}: {resources[items]}g")
            else:
                print(f"{items.title()}: {resources[items]}ml")
        print(f"Money: ${total_money}")

    elif choice in ("latte", "cappuccino", "espresso"):
        call_report()
        checking_resources = check_resources_sufficiency(report)
        if checking_resources[0]:
            customer_amount = round(process_coins(choice), 2)
            transaction_summary = check_transaction_sufficiency()
            if transaction_summary[1]:
                modified_report(resources)
                total_money += transaction_summary[2]
                print(transaction_summary[0])
            else:
                print(transaction_summary[0])
        else:
            machine_operation = False
            print(f"Sorry there is not enough {checking_resources[1]}.")

    elif choice == "off":
        machine_operation = False

    else:
        print("Invalid Input")







