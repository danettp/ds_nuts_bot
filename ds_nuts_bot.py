# D's Nuts Bot program
# (21/03/22)
# Bugs - Phone number input allows letters
#      - name input allows numbers


import sys
import random
from random import randint 
#Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10

#List of random names
names = ["Jack", "Rachel", "Michelle", "Aaron", "Samuel", "An", "Julie", "Jerry", "Jace", "Sofia"]
# list of nuts names
nuts_names = ["Peanuts","Pistachios", "Macadamia", "Almonds", "Cashews", "Walnuts", "Pecans", "Hazelnuts", 
              "Brazil Nuts", "Pine Nuts", "Chestnuts", "Mixed Nuts"]
# list of nuts prices
nuts_prices = [8.00, 8.00, 8.00, 9.50, 9.50, 9.50, 9.50, 15.00, 
               15.00, 15.00, 15.50, 19.00]
#list to store ordered nutss
order_list = []
#list to store nuts prices
order_cost = []
#Customer details dictionary
customer_details = {}

# validates inputs to check if they are blank
def not_blank(question):
    valid =  False
    while not valid: 
        response = input (question)
        if response != "": 
            return response.title()
        else:
            print("This cannot be blank.")

# validates inputs to check if they are string
def valid_string(question):
    #Asks a question and makes sure that the answer is alphabetical. Returns the string.
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters.")
        else:
            return response.title()

# validates inputs to check if they are an integer
def val_int(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}")
        except ValueError:
            print("That is not a valid number.")
            print(f"Please enter a number between {low} and {high}")

# validates inputs to check if it is an appropriate phone number
def valid_phone(question, PH_LOW, PH_HIGH):
    while True:
        try:
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return str(num)
            else: 
                print("NZ phone numbers have between 7 to 10 digits")
        except ValueError:
            print("Please enter a number")

# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to D's Nuts ***")
    print("*** My name is {} ***".format(name))
    print("*** I will be here to help you order your delicious organic nuts ***")


# Menu for delivery or click and collect
def order_type():
    del_collect = ""
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Is your order for click and collect or delivery?")
    print("(1) Click and Collect")
    print("(2) Delivery")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print("Click and Collect")
        click_and_collect()
        del_pick = "Click and Collect"
    else:
        print("Delivery")
        delivery_info()
        del_pick = "Delivery"
    return del_pick

    

# Click and collect information - name and phone number
def click_and_collect():
    #Basic Instructions 
    question = ("Please enter your name ")
    customer_details["name"] = valid_string(question)
    print(customer_details["name"])

    question = ("Please enter your phone number ")
    customer_details['phone'] = valid_phone(question, PH_LOW, PH_HIGH)
    print(customer_details["phone"])
    print(customer_details)


# Delivery information - name, phone number and address
def delivery_info(): 
    question = ("Please enter your name ")
    customer_details["name"] = valid_string(question)
    print(customer_details["name"])

    question = ("Please enter your phone number ")
    customer_details['phone'] = valid_phone(question, PH_LOW, PH_HIGH)
    print(customer_details["phone"])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print(customer_details["house"])

    question = ("Please enter your street name ")
    customer_details['street'] = valid_string(question)
    print(customer_details["street"])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = valid_string(question)
    print(customer_details["suburb"])
    print(customer_details)




# Nuts Menu
def menu():
    print("-"*60)
    print("========= MENU ==========")
    print("-"*60)

    for count in range (len(nuts_names)):
        print("({}) {} ${:.2f}" .format(count+1, nuts_names[count], nuts_prices[count]))
    
    print("-"*60)




# Choose total number of items - max 12
# Nuts order - from menu - print each nut ordered with cast

def order_nuts():
    # ask for total number of nuts
    num_nuts = 0
    LOW = 1
    HIGH = 12
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print("How many nuts do you want to orer?")
    num_nuts = val_int(LOW, HIGH, question)
    # Choose nuts from menu
    for item in range(num_nuts):
        while num_nuts > 0:
            print("Please choose your nuts by" 
                  " entering the number from the menu ")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            nuts_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            nuts_ordered = nuts_ordered-1
            order_list.append(nuts_names[nuts_ordered])
            order_cost.append(nuts_prices[nuts_ordered])
            print("{} ${:.2f}" .format(nuts_names[nuts_ordered],
                   nuts_prices[nuts_ordered]))
            num_nuts = num_nuts-1


# Print order out - including if the order is delivery or click and collect and names 
# and price of each nut - total cost including any delivery charge
def print_order(del_collect):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_collect == "Click and Collect":
        print("Your order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_collect == "Delivery":
        print("Your order is for Delivery")
        print(f"Customer Name: {customer_details['name']}"
        f"\nCustomer Phone: {customer_details['phone']}"
        f"\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")


# Ability to cancel or proceed with order
def confirm_cancel():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please confirm your order - Choose: ")
    print("(1) To Confirm")
    print("(2) To Cancel")
    print("Please enter a number ")

    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print("Order Confirmed")
        print("Your order has been sent to our kitchen")
        print("Your delicious nuts will be with you shortly")
        new_exit()
    elif confirm == 2:
        print("Your Order has been Cancelled")
        print("You can restart your order or exit the BOT")
        new_exit()

print("")


# Option for new order or to exit
def new_exit():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Do you want to start another order or exit? Choose: ")
    print("(1) To start another order")
    print("(2) To exit the BOT ")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()
    elif confirm == 2:
        print("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()


# Main function 
def main():
    '''
    Purpose: To run all functions
    Parameters: None
    Returns: None
    '''
    welcome()
    del_collect = order_type()
    print(del_collect)
    menu()
    order_nuts()
    print_order(del_collect)
    confirm_cancel()
    new_exit()


main()