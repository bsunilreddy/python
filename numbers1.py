#numbers1.py
#program for generating 1 to n numbers, where n  is +ve. if n is -ve, generate -1 ,-2...-n
n=int(input("Enter Value of n:"))
if (n==0):
	print("n is invalid input")
else:
	print("="*50)
	print("Number within {}".format(n))
	print("="*50)
	i=1
	while(i<=n):
		print("\t{}".format(i))
		i=i+1
	else: 
		j=-1   # n=-10
		while(j>=n):
			print("\t{}".format(j))
			j-=1
		print("*"*50)	
