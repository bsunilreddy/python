
n=int(input("enter how many tables you want"))

if(n<=0):
	print("enter valid input")

else:
	print("enter the tables by using space")
	#tables=[int(val)for val in input().split()]
	for val in range(int(input()),int(input())):
		print("\t {} * {}= {}".format(n,val,val*n))