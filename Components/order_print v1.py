#list to store ordered pizzas
order_list = ["Peanuts","Pistachios", "Macadamia", "Almonds"]
#list to store pizza prices
order_cost = [8.00, 8.00, 8.00, 9.50]


count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1 

    