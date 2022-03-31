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

# validates house number input to check if they are an integer
def val_house(question):
    while True:
        try:
            userInput = int(input(question))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput 


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