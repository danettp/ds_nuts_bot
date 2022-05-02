# D's Nuts Bot

# Libraries
import sys
import random
from random import randint
# My Libraries
from validations import *   # Import Validation functions
# Constants
LOW = 1
HIGH = 2


class readFromFiles:
    # Lists read from files
    try:
        # if it can open, continue code
        nuts = list()  # list for total nuts
        with open("nuts.txt") as x:  # open nuts.txt and import as list
            for line in x:
                nuts.append(line.rstrip('\n'))  # strips \n from entry
    except IOError:
        # if file isnt found then end
        print("The File > nuts.txt < doesn't exist!"
              "Please doublecheck and try again.")
        exit()

    try:
        prices = list()  # list for all prices
        with open("prices.txt") as x:  # open prices.txt and import as list
            for line in x:
                prices.append(line.rstrip('\n'))  # strips \n from entry
    except IOError:
        # if file isnt found then end
        print("The File > prices.txt < doesn't exist!"
              "Please doublecheck and try again.")
        exit()

# Call variables from classes
newReader = readFromFiles
# List of random names
names = ["Steve", "Rachel", "Michelle", "Aaron",
         "Ben", "An", "Julie", "Terry", "Daniel", "Sofia"]
# list to store ordered nutss
order_list = []
# list to store nuts prices
order_cost = []
# Customer details dictionary
customer_details = {}


# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out
    a welcome message
    Parameters: None
    Returns: None
    '''
    num = randint(0, 9)
    name = (names[num])
    # prints (formatted) welcome message
    print("*** Welcome to D's Nuts! ***")
    print("*** My name is {} ***".format(name))
    print("*** I will be here to help you order"
          "your delicious organic nuts ***")


# Menu for delivery or click and collect
def order_type():
    del_collect = ""  # sets del_collect default to blank string
    # asks for input(int) - between LOW and HIGH
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print ("Is your order for click and collect or delivery?")
    print("(1) Click and Collect")
    print("(2) Delivery")
    # takes LOW, HIGH, and question as parameter
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:  # If (1) click and collect chosen...
        print("Click and Collect")
        click_and_collect()  # calls click and collect information function
        del_pick = "Click and Collect"  # sets del_collect to click and collect
    else:  # if (2) delivery chosen...
        print("Delivery")
        delivery_info()  # calls delivery information function
        del_pick = "Delivery"  # sets del_collect to delivery
    return del_pick  # returns del_pick back to main() function


# Click and collect information - name and phone number
def click_and_collect():
    # Basic Instructions
    question = ("Please enter your name ")
    customer_details["name"] = valid_string(question)  # asks for input(string)
    print(customer_details["name"])

    question = ("Please enter your phone number ")
    # asks for input(integer)
    customer_details['phone'] = valid_phone(question)
    print(customer_details["phone"])


# Delivery information - name, phone number and address
def delivery_info():
    # Basic Instructions
    question = ("Please enter your name ")
    customer_details["name"] = valid_string(question)  # asks for input(string)
    print(customer_details["name"])

    question = ("Please enter your phone number ")
    # asks for input(integer)
    customer_details['phone'] = valid_phone(question)
    print(customer_details["phone"])

    question = ("Please enter your house number ")
    customer_details['house'] = val_house(question)  # asks for input(integer)
    print(customer_details["house"])

    question = ("Please enter your street name ")
    # asks for input(string)
    customer_details['street'] = valid_string(question)
    print(customer_details["street"])

    question = ("Please enter your suburb ")
    # asks for input(string)
    customer_details['suburb'] = valid_string(question)
    print(customer_details["suburb"])


# Nuts menu
def menu():
    # Title
    print("-"*60)
    print("Nuts Options Today:")
    print("-"*60)
    # Formatting menu (names and prices)
    for x in range(0, len(newReader.nuts)):
        print("({}) {} - ${:.2f}".format(x+1,
              newReader.nuts[x], float(newReader.prices[x])))
    print("-"*60)


# Choose total number of items - max 12
# Nuts order - from menu - print each nut ordered with cast
def order_nuts():
    # asks for input(integer)
    num_nuts = val_int(1, 12, "How many nuts would you like (1-12)? ")
    print("Please select {} nut(s).".format(num_nuts))
    for x in range(0, num_nuts):  # if in range... (select a nut)
        nuts_ordered = val_int(1, (len(newReader.nuts)),
                                  ("Please select nut {}: ".format(x+1)))
        # print chosen nut (added to order)
        print("Added {} (${:.2f}) to your order."
              .format(newReader.nuts[nuts_ordered-1],
                      float(newReader.prices[nuts_ordered-1])))
        order_list.append(newReader.nuts[nuts_ordered-1])
        order_cost.append(float(newReader.prices[nuts_ordered-1]))


# Print order out - including if the order is
# delivery or click and collect and names
# and price of each nut - total cost including any delivery charge
# takes del_collect as parameter
def print_order(del_collect):
    # Format Customer Details
    print("-"*60)
    print("Customer Details:")
    print("-"*60)
    # If click and collect, print you will recieve text
    if del_collect == "Click and Collect":
        print("Your order is for Click and Collect")
        print("")
        print("You will recieve a text message when"
              " your nuts are ready to be picked up.")
        print("")
        # Format to print customer click and collect details
        print(f"Customer Name: {customer_details['name']}"
              f"\nCustomer Phone: {customer_details['phone']}")
        print("-"*60)
    elif del_collect == "Delivery":  # if delivery, run below
        # Handle delivery
        # if <5 nuts ordered, $9 added, but 5> free of charge
        if len(order_list) < 5:
            print("An extra $9.00 will be added for delivery.")
            order_cost.append(9)  # adds $9 to charge if ordered 4 or less nuts
            print("")
        print("Your order is for Delivery")
        # prints delivery details/information
        print(f"Customer Name: {customer_details['name']}"
              f"\nCustomer Phone: {customer_details['phone']}"
              f"\nCustomer Address: {customer_details['house']}"
              f" {customer_details['street']} {customer_details['suburb']}")
        print("-"*60)
    print("Your Order Details:")
    print("-"*60)
    count = 0
    # print ordered items
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format
              (item, float(order_cost[count])))
        count = count+1
    print()
    # Calculate Total Cost
    total_cost = sum(order_cost)  # takes order_cost as parameter
    # Print Total Cost (formatted)
    print("Total Cost: ${:.2f}".format(total_cost, 2))


# Ability to cancel or proceed with order
def confirm_cancel():
    # asks for input(integer)
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print("-"*60)
    print ("Please confirm your order - Choose: ")
    print("(1) To Confirm")
    print("(2) To Cancel")

    # takes LOW, HIGH, and question as parameter
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:  # if order is confirmed (1) prints order confirmed
        print("-"*60)
        print("Order Confirmed")
        print("Your order is getting picked and packed.")
        print("Your delicious nuts will be with you soon.")
        print("-"*60)
        new_exit()  # calls new_exit() function
    elif confirm == 2:  # if order is cancelled (2) prints order cancelled
        print("-"*60)
        print("Your Order has been Cancelled")
        print("-"*60)
        print("You can restart your order or exit the BOT")
        new_exit()  # calls new_exit() function


# Option for new order or to exit
def new_exit():
    # asks for input(integer)
    question = (f"Enter a number between {LOW} and {HIGH}: ")
    print ("Do you want to start another order or exit? Choose: ")
    print("(1) To start another order")
    print("(2) To exit the BOT ")
    # takes LOW, HIGH, and question as parameter
    confirm = val_int(LOW, HIGH, question)
    # if confirm (1), prints New Order
    # and clears all temporary lists and details
    if confirm == 1:
        print("New Order")
        # clear temporary lists
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()  # calls main() function
    # if exit (2), prints Exit and
    # clears all temporary lists and details
    elif confirm == 2:
        print("Exit")
        # clear temporary lists
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit()  # exits and stops system


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
    print_order(del_collect)  # takes del_collect as parameter
    confirm_cancel()
    new_exit()

main()
