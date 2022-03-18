# D's Nuts Bot program
import random
from random import randint 

#List of random names
names = ["Jack", "Rachel", "Michelle", "Randy", "Samuel", "An", "Julie", "Jerry", "Jace", "Sofia"]
#Customer details dictionary
customer_details = {}

# validates inputs to check if they are blank
def not_blank(question):
    valid =  False
    while not valid: 
        response = input (question)
        if response != "": 
            return response
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
    print("*** My name is", name, " ***")
    print("*** I will be here to help you order your delicious organic nuts ***")


# Menu for delivery or click and collect
def order_type():
    print ("Is your order for click and collect or delivery?")

    print("For click and collect please enter 1")
    print("For delivery please enter 2")

    while True:
        try: 
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Click and Collect")
                    break
                
                elif delivery == 2:
                    print("Delivery")
                    break
            else: 
                print("The number must be 1 or 2")
        except ValueError:
            print("That is not a valid number.")
            print("Please enter 1 or 2")




# Click and collect information - name and phone number
def click_and_collect():
    #Basic Instructions 
    question = ("Please enter your name ")
    customer_details["name"] = not_blank(question)
    print(customer_details["name"])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details["phone"])





# Delivery information - name, phone number and address





# Choose total number of items - max 5






# Nuts Menu






# Item (nuts) order - from menu - print each nut ordered with cast





# Print order out - including if the order is delivery or click and collect and names 
# and price of each nut - total cost including any delivery charge




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
    click_and_collect()
    order_type()


main()