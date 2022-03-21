# list of nuts names
nuts_names = ["Peanuts","Pistachios", "Macadamia", "Almonds", "Cashews", "Walnuts", "Pecans", "Hazelnuts", 
              "Brazil Nuts", "Pine Nuts", "Chestnuts", "Mixed Nuts"]

# list of nuts prices
nuts_prices = [8.00, 8.00, 8.00, 9.50, 9.50, 9.50, 9.50, 15.00, 
               15.00, 15.00, 15.50, 19.00]

#list to store ordered nuts
order_list = []
#list to store nuts cost
order_cost = []

#list to store order cost

def menu():
    print("-"*60)
    print("========= MENU ==========")
    print("-"*60)

    for count in range (len(nuts_names)):
        print("({}) {} ${:.2f}" .format(count+1, nuts_names[count], nuts_prices[count]))
    
    print("-"*60)

menu()


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

menu()
order_nuts()
