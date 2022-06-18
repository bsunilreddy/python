n=int(input("Enter a number:"))
if(n<=0):
	print("{} is invalid input:".format(n))
else:
	print("-"*50)
	print("Even Numbers within {}:".format(n))
	print("-"*50)
	i=2
	while(i<=n):
		print("{}".format(i), end=" ")
		i+=2
	else:
		print()
		print("-"*50)