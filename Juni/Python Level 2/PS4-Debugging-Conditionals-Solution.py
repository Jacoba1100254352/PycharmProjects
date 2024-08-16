numTickets = int(input("How many tickets did you win? "))

lollipopPrice = 10
actionFigurePrice = 75
tshirtPrice = 250
stuffedAnimalPrice = 350

# Print out which items you can afford, and how many tickets you'd have left if you bought it
if numTickets < lollipopPrice and numTickets < actionFigurePrice and numTickets < tshirtPrice and numTickets < stuffedAnimalPrice:
	print("You can't afford anything by yourself")
if numTickets >= lollipopPrice:
	print("You can buy a lollipop, but you'll only have " + str(numTickets - lollipopPrice) + " tickets left")
if numTickets >= actionFigurePrice:
	print("You can buy an action figure, but you'll only have " + str(numTickets - actionFigurePrice) + " tickets left")
if numTickets >= tshirtPrice:
	print("You can buy a t-shirt, but you'll only have " + str(numTickets - tshirtPrice) + " tickets left")
if numTickets >= stuffedAnimalPrice:
	print(
		"You can buy a stuffed animal, but you'll only have " + str(numTickets - stuffedAnimalPrice) + " tickets left")

# You and Kant want to buy matching t-shirts, but he is short 6 tickets. Can you afford to loan him 6 tickets and still buy a t-shirt yourself?
# If you can't afford to get two t-shirts, can you afford to get just one? (remember Kant already has 244 tickets)
if numTickets >= tshirtPrice + 6:
	print("You can get matching t-shirts!")
elif numTickets >= tshirtPrice:
	print("Sorry, you can't get matching t-shirts, but you can afford a single t-shirt!")
