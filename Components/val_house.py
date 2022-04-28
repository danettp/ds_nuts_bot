def val_house(question):
    while True:
        try:
            userInput = int(input(question))       
        except ValueError:
            print("Not an integer! Please enter a number.")
            continue
        else:
            return userInput 