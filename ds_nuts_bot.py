# D's Nuts Bot program

import random
from random import randint 

#List of random names
names = ["Jack", "Rachel", "Michelle", "Randy", "Samuel", "An", "Julie", "Jerry", "Jace", "Sofia"]

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
def collect_menu():
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





# Delivery information - name, phone number, and address






# Delivery information - name and phone





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
    collect_menu()


main()