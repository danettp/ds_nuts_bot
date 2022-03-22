# D's Nuts Bot program
# (21/03/22)
# Bugs - Phone number input allows letters
#      - name input allows numbers


import random
from random import randint 

#List of random names
names = ["Jack", "Rachel", "Michelle", "Aaron", "Samuel", "An", "Julie", "Jerry", "Jace", "Sofia"]
# list of nuts names
nuts_names = ["Peanuts","Pistachios", "Macadamia", "Almonds", "Cashews", "Walnuts", "Pecans", "Hazelnuts", 
              "Brazil Nuts", "Pine Nuts", "Chestnuts", "Mixed Nuts"]
# list of nuts prices
nuts_prices = [8.00, 8.00, 8.00, 9.50, 9.50, 9.50, 9.50, 15.00, 
               15.00, 15.00, 15.50, 19.00]
#list to store ordered pizzas
order_list = []
#list to store pizza prices
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
    print ("Is your order for click and collect or delivery?")

    print("For click and collect please enter 1")
    print("For delivery please enter 2")

    while True:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Click and Collect")
                    click_and_collect()
                    del_collect = "click and collect"
                    break   
                elif delivery == 2:
                    print("Delivery")
                    delivery_info()
                    del_collect = "delivery"
                    break
            else: 
                print("The number must be 1 or 2")
    return del_collect

    



# Click and collect information - name and phone number
def click_and_collect():
    #Basic Instructions 
    question = ("Please enter your name ")
    customer_details["name"] = not_blank(question)
    print(customer_details["name"])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details["phone"])
    print(customer_details)





# Delivery information - name, phone number and address
def delivery_info(): 
    question = ("Please enter your name ")
    customer_details["name"] = not_blank(question)
    print(customer_details["name"])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details["phone"])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print(customer_details["house"])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print(customer_details["street"])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
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
    while True:
        try:
            num_nuts = int(input("How many nuts do you want to order? "))
            print(num_nuts)
            if num_nuts >= 1 and num_nuts <= 12:
                break
            else:
                print("Your order must be between 1 and 12")
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number between 1 and 12 ")
    # Choose nuts from menu
    for item in range(num_nuts):
        while num_nuts > 0:
            while True:
                try:
                    nuts_ordered = int(input("Please choose your nuts by entering the number from the menu "))
                    if nuts_ordered >= 1 and nuts_ordered <= 12:
                        break
                    else:
                        print("Your nuts order must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 12")  
            nuts_ordered = nuts_ordered-1
            order_list.append(nuts_names[nuts_ordered])
            order_cost.append(nuts_prices[nuts_ordered])
            print("{} ${:.2f}" .format(nuts_names[nuts_ordered],nuts_prices[nuts_ordered]))
            num_nuts = num_nuts-1



# Print order out - including if the order is delivery or click and collect and names 
# and price of each nut - total cost including any delivery charge
def print_order(del_collect):
    print()
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_collect == "click and collect":
        print("Your order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_collect == "delivery":
        print("Your order is for Delivery")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}" 
              f"\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1 
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

# Ability to cancel or proceed with order





# Option for new order or to exit







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


main()