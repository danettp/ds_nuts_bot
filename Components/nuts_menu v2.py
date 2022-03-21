# list of nuts names
nuts_names = ["Peanuts","Pistachios", "Macadamia", "Almonds", "Cashews", "Walnuts", "Pecans", "Hazelnuts", 
                "Brazil Nuts", "Pine Nuts", "Chestnuts", "Mixed Nuts"]

# list of nuts prices
nuts_prices = [8.00, 8.00, 8.00, 9.50, 9.50, 9.50, 9.50, 15.00, 15.00, 15.00, 15.50, 19.00]


def menu():
    number_nuts = 12
    for count in range (number_nuts):
        print("{} {} ${:.2f}" .format(count+1, nuts_names[count], nuts_prices[count]))


menu()
