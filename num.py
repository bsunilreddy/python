i=int(input("Enter the table= "))
k=int(input("Enther the value upto= "))
if(i<=0):
	print("Enter the valid input")

else:
	n=1
	while(n<=k):
		print("the vlaue of {} * {} = {}".format(i,n,i*n))
		n=n+1
	