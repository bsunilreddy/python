#sum of a given digit
n=int(input("enter a digit for total"))
if(n<=0):
	print("enter a valid input")
else:
	s=0
	while(n>0):
		d=n%10
		s=s+d 
		n=n//10
	else:
		print(" the sum of  the given number is ={} ".format(s))
