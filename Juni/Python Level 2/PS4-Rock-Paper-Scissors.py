user1 = input('Player 1, please pick rock, paper, or scissors: ')
user2 = input('Player 2, please pick rock, paper, or scissors: ')

if user1 == 'rock':
	if user2 == 'rock':
		print('Tie!')
	elif user2 == 'paper':
		print('Player 2 wins!')
	elif user2 == 'scissors':
		print('Player 1 wins!')
	else:
		print('Player 2 did not pick rock, paper, or scissors. Player 1 wins!')

elif user1 == 'paper':
	if user2 == 'rock':
		print('Player 1 wins!')
	elif user2 == 'paper':
		print('Tie!')
	elif user2 == 'scissors':
		print('Player 2 wins!')
	else:
		print('Player 2 did not pick rock, paper, or scissors. Player 1 wins!')

elif user1 == 'scissors':
	if user2 == 'rock':
		print('Player 2 wins!')
	elif user2 == 'paper':
		print('Player 1 wins!')
	elif user2 == 'scissors':
		print('Tie!')
	else:
		print('Player 2 did not pick rock, paper, or scissors. Player 1 wins!')

else:
	print('Player 1 did not pick rock, paper, or scissors. Player 2 wins!')
