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


main()