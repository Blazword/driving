country = input('which country you came from: ')
age = input('How old are you: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive.')
	else:
		print('You can\'t drive yet.')