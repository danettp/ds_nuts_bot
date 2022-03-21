#list to store ordered pizzas
order_list = ["Peanuts","Pistachios", "Macadamia", "Almonds"]
#list to store pizza prices
order_cost = [8.00, 8.00, 8.00, 9.50]

customer_details= {'name':'Danett','phone':'08102312','house':'45','street':'Harry','suburb':'Howick'}



#print("\n",customer_details['name'],"\n", customer_details['phone'], "\n", customer_details['house'], "\n", customer_details['street'], "\n", customer_details['suburb'])

print("\n Customer name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Street Suburb:\n{}".format( customer_details['name'], customer_details['phone'], customer_details['house'], customer_details['street'], customer_details['suburb']))


count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1 