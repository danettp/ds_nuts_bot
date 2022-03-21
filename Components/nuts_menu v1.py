nuts_names = ["Peanuts","Pistachios", "Macadamia", "Almonds", "Cashews", "Walnuts", "Pecans", "Hazelnuts", 
                "Brazil Nuts", "Pine Nuts", "Chestnuts", "Mixed Nuts"]



nuts_prices = [8.00, 8.00, 8.00, 9.50, 9.50, 9.50, 9.50, 15.00, 15.00, 15.00, 15.50, 19.00]

number_nuts = 12

# print ("How many nuts would you like to order? ")
# num_pizza = in(input())

for count in range (number_nuts):
    print(count, nuts_names[count], nuts_prices[count])


