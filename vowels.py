alp = str(input())

if((alp>='a'and alp<='z') or (alp>='A' and alp<='Z')):
	if((alp=='a') or (alp=='e') or (alp=='i') or (alp=='o') or (alp=='u') or (alp=='A') or (alp=='E') or (alp=='I') or (alp=='O') or (alp=='U')):

		print("Vowels")

	else:

		print("Consonants")

else:
	print("Invalid")