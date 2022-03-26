def valid_string(question):
    #Asks a question and makes sure that the answer is alphabetical. Returns the string.
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Input must only contain letters.")
        else:
            return response.title()


question = "Please enter your name "
name = valid_string(question)
print(name)

