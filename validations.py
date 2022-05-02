# validates inputs to check if they are blank
# takes question as parameter
# returns response in title class if valid


def not_blank(question):
    valid = False
    while not valid:  # sets up while loop
        response = input(question)  # asks for input(string)
        if response != "":
            return response  # if blank, returns response
        else:
            print("This cannot be blank.")


# validates inputs to check if they are string
# takes question as parameter
# returns response in title class if valid
def valid_string(question):
    # Asks a question and makes sure that the answer is alphabetical.
    # Returns the string.
    while True:  # sets up while loop
        response = input(question)  # asks for input(string)
        x = response.isalpha()
        if x is False:  # if x is False prints error message
            print("Input must only contain letters.")
        else:
            return response.title()  # if True returns response in title class


# validates inputs to check if they are an integer
# takes low, high, and question as parameter
def val_int(low, high, question):
    while True:  # sets up while loop
        try:
            num = int(input(question))  # asks for input(integer)
            # only accept if number is between/equal low and high
            if num >= low and num <= high:
                return num  # returns response
            else:
                print(f"Please enter a number between {low} and {high}")
        except ValueError:  # if input is invalid print error message
            print("That is not a valid number.")
            print(f"Please enter a number between {low} and {high}")


# validates house number input to check if they are an integer
# takes question as parameter
def val_house(question):
    while True:  # sets up while loop
        try:
            userInput = int(input(question))  # asks for input(integer)
        # if user input is invalid, prints error message
        except ValueError:
            print("That is not a valid number. Please enter input again.")
            continue
        else:
            return userInput  # returns response


# validates inputs to check if it is an appropriate phone number
# takes question as parameter
def valid_phone(question):
    while True:  # sets up while loop
        try:
            num = int(input(question))  # asks for input(integer)
            test_num = num  # define variable to be tested
            count = 0  # how many digits in an integer
            while test_num > 0:  # if number > 0...
                test_num = test_num//10
                count = count + 1
            # only accept if phone number has 7 to 10 digits
            if count >= 7 and count <= 10:
                return str(num)  # returns response
            # if number is <7 digits or 10> digits, prints error message
            else:
                print("NZ phone numbers have between 7 to 10 digits")
        except ValueError:  # if input is invalid print error message
            print("Please enter a number")
