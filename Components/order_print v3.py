#list to store ordered pizzas
order_list = ["Peanuts","Pistachios", "Macadamia", "Almonds"]
#list to store pizza prices
order_cost = [8.00, 8.00, 8.00, 9.50]

customer_details= {'name':'Danett','phone':'08102312','house':'45','street':'Harry','suburb':'Howick'}

#print("Customer name: {} \nCustomer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Street Suburb:\n{}".format( customer_details['name'], customer_details['phone'], customer_details['house'], customer_details['street'], customer_details['suburb']))

print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}" 
      f"\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")





count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1 

