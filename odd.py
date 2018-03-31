count = int(input("how many odd numbers you want to print: "))
for counter in range(0, count*2):
	if(counter%2 == 1):
		print(counter)