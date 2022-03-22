print ("Do you want to start another order or exit? Choose: ")
print("(1) To start another order")
print("(2) To exit the BOT")
while True:
    try: 
        confirm = int(input("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print("New Order")
                break
            
            elif confirm == 2:
                print("Exit")
                break
        else: 
            print("The number must be 1 or 2")
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2")

        