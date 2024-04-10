numTickets = int(input("How many tickets did you win? "))

lollipopPrice = 10
actionFigurePrice = 75
tshirtPrice = 250
stuffedAnimalPrice = 350

# Print out which items you can afford, and how many tickets you'd have left if you bought it
if numTickets < lollipopPrice or numTickets < actionFigurePrice and numTickets < tshirtPrice or numTickets < stuffedAnimalPrice:
	print("You can't afford anything by yourself")
elif numTickets > lollipopPrice:
	print("You can buy a lollipop, but you'll only have " + str(numTickets - lollipopPrice) + " tickets left")
elif numTickets > actionFigurePrice:
	print("You can buy an action figure, but you'll only have " + str(numTickets - actionFigurePrice) + " tickets left")
elif numTickets > tshirtPrice:
	print("You can buy a t-shirt, but you'll only have " + str(numTickets - tshirtPrice) + " tickets left")
else:
	print(
		"You can buy a stuffed animal, but you'll only have " + str(numTickets - stuffedAnimalPrice) + " tickets left")

# You and Kant want to buy matching t-shirts, but he is short 6 tickets. Can you afford to loan him 6 tickets and still buy a t-shirt yourself?
# If you can't afford to get two t-shirts, can you afford to get just one? (remember Kant already has 244 tickets)
if numTickets > tshirtPrice and numTickets > tshirtPrice + 6:
	print("You can get matching t-shirts!")
if numTickets >= 6:
	print("Sorry, you can't get matching t-shirts, but you can afford a single t-shirt!")
