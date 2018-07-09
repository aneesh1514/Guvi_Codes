a=input()
if type(a)==str:
	if a in ['a','e','i','o','u']:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")