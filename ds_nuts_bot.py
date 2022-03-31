# D's Nuts Bot program

# Libraries
import sys
import random
from random import randint 
#My Libraries
from validations import * #Import Validation functions
#Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10

class readFromFiles:
    #Lists read from files
    try:
        #if it can open, continue code
        nuts = list() #list for total nuts
        with open("nuts.txt") as x: #open nuts.txt and import as list
            for line in x:
                nuts.append(line.rstrip('\n')) #strips \n from entry 
    except IOError:
        #if file isnt found then end
        print("The File > nuts.txt < doesn't exist! Please doublecheck and try again.")
        exit()

    try:
        prices = list() #list for all prices
        with open("prices.txt") as x: #open prices.txt and import as list
            for line in x:
                prices.append(line.rstrip('\n')) #strips \n from entry 
    except IOError:
        #if file isnt found then end
        print("The File > prices.txt < doesn't exist! Please doublecheck and try again.")
        exit()

#Call variables from classes
newReader = readFromFiles
#List of random names
names = ["Jack", "Rachel", "Michelle", "Aaron", "Samuel", "An", "Julie", "Jerry", "Jace", "Sofia"]
#list to store ordered nutss
order_list = []
#list to store nuts prices
order_cost = []
#Customer details dictionary
customer_details = {}

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
    print("*** Welcome to D's Nuts! ***")
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
    customer_details['house'] = val_house(question)
    print(customer_details["house"])

    question = ("Please enter your street name ")
    customer_details['street'] = valid_string(question)
    print(customer_details["street"])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = valid_string(question)
    print(customer_details["suburb"])
    print(customer_details)

# Nuts menu
def menu():
    # Title
    print("-"*60)
    print("Nuts Options Today:")
    print("-"*60)
    # Menu
    for x in range(0,len(newReader.nuts)):
        print("({}) {} - ${:.2f}".format(x+1,newReader.nuts[x],float(newReader.prices[x])))
    print("-"*60)


# Choose total number of items - max 12
# Nuts order - from menu - print each nut ordered with cast
def order_nuts():
    num_nuts = val_int(1,12,"How many nuts would you like (1-12)? ")
    print("Please select {} nut(s).".format(num_nuts))
    for x in range(0,num_nuts): 
        nuts_ordered = val_int(0,(len(newReader.nuts)-1),("Please select nut {}: ".format(x+1)))
        print("Added {} (${:.2f}) to your order.".format(newReader.nuts[num_nuts], float(newReader.prices[x])))
        order_list.append(newReader.nuts[nuts_ordered])
        order_cost.append(float(newReader.prices[nuts_ordered]))

# Print order out - including if the order is delivery or click and collect and names 
# and price of each nut - total cost including any delivery charge
def print_order(del_collect):
    print("-"*60)
    print("Customer Details:")
    print("-"*60)
    if del_collect == "Click and Collect":
        print("Your order is for Click and Collect")
        print("You will recieve a text message when your nuts are ready to be picked up.")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
        print("-"*60)
    elif del_collect == "Delivery":
        # Handle delivery
        if len(order_list) < 5:
            print("An extra $9.00 will be added for delivery.")
            order_cost.append(9)
        print("Your order is for Delivery")
        print(f"Customer Name: {customer_details['name']}"
        f"\nCustomer Phone: {customer_details['phone']}"
        f"\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
        print("-"*60)
    print("Your Order Details:")
    print("-"*60)
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item,float(order_cost[count])))
        count = count+1
    print()
    # Calc Total Cost
    total_cost = sum(order_cost)
    # Print Total Cost
    print("Total Cost: ${:.2f}".format(total_cost,2))
    print("-"*60)


# Ability to cancel or proceed with order
def confirm_cancel():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print("-"*60)
    print ("Please confirm your order - Choose: ")
    print("(1) To Confirm")
    print("(2) To Cancel")
    print("Please enter a number ")

    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print("-"*60)
        print("Order Confirmed")
        print("Your order is getting picked and packed.")
        print("Your delicious nuts will be with you shortly.")  
        print("-"*60)
        new_exit()
    elif confirm == 2:
        print("-"*60)
        print("Your Order has been Cancelled")
        print("-"*60)
        print("You can restart your order or exit the BOT")
        new_exit()

# Option for new order or to exit
def new_exit():
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