#tables
n=int(input("enter how many tables you want"))
if(n<=0):
	print("enter valid input")
else:
	for val in range(int(input()),int(input())):

		print(" {} * {} = {}".format(n,val,val*n))
