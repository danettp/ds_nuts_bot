print ("Please confirm your order - Choose: ")
print("(1) To Confirm")
print("(2) To Cancel")
while True:
    try: 
        confirm = int(input("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print("Order Confirmed")
                print("Your order for nuts is getting packed and prepared.")
                break
            
            elif confirm == 2:
                print("Your Order has been Cancelled")
                print("You can restart your order or exit the BOT")
                break
        else: 
            print("The number must be 1 or 2")
    except ValueError:
        print("That is not a valid number.")
        print("Please enter 1 or 2")

        