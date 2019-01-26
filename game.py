import random
losowa = random.randint(1, 100)
print ('Guess This Number!!!!!')
print ('I Have A Number Between 1 And 100. You just have to Guess until You Guess corectly. EASY!!!')
odp = int(input('Your Guess: '))
tries = 1
while losowa != odp:
	if odp > losowa:
		print ('Too Big!')
	else:
		print ('Too Small!')
	odp = int(input('Your Guess: ')
	tries += 1
print ('Bravo!!!! The number was', losowa, '! And you just needed', tries, 'tries!')