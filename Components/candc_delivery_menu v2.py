# Bugs
# will only work for valid input "d" and "c"
# invalid input triggers else statement but program does not ask for input again.

# menu so that user can choose either click and colelct or delivery

print ("Do you want your order delivered or are you click and collecting it?")

print("For delivery press enter d or enter c for click & collect.")

delivery = input()

if delivery == "d":
    print("Delivery")

elif delivery == "c":
    print("Click & Collect")

else:
    print("That was not a valid input.")
    