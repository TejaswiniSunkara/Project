count = int(("how many even numbers you want to print: "))
print(count+" even numbers are: ")
for counter in range(0, count*2):
	if(counter%2==0):
		print(counter)
