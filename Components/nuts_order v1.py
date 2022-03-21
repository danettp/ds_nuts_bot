# list of nuts names
nuts_names = ["Peanuts","Pistachios", "Macadamia", "Almonds", "Cashews", "Walnuts", "Pecans", "Hazelnuts", 
              "Brazil Nuts", "Pine Nuts", "Chestnuts", "Mixed Nuts"]

# list of nuts prices
nuts_prices = [8.00, 8.00, 8.00, 9.50, 9.50, 9.50, 9.50, 15.00, 
               15.00, 15.00, 15.50, 19.00]

#list to store ordered nuts
order_list = []
#list to store pizza nuts
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

# ask for total number of nuts
num_nuts = 0

num_nuts = int(input("How many nuts do you want to order? "))

print(num_nuts)

# Choose pizzas from menu
print("Please choose your nuts by entering the number from the menu ")
for item in range(num_nuts):
    while num_nuts > 0:
        nuts_ordered = int(input())
        order_list.append(nuts_names[nuts_ordered])
        order_cost.append(nuts_prices[nuts_ordered])
        num_nuts = num_nuts-1

print(order_list)
print(order_cost)


# Count down until all pizzas are ordered



# print order