#program for sal and details
eno=int(input("Enter the employee Number:"))
ename=(input("Enter the employee Name:"))
esal=float(input("Enter the employee salary:"))
if(esal>10000):
	a=esal*(20/100)
	b=esal*(10/100)
	c=esal*(30/100)
else:
	if(esal<10000):
		a=esal*(23/100)
		b=esal*(16/100)
		c=esal*(37/100)
    else:
		if(esal=10000):
			a=esal*(56/100)
			b=esal*(45/100)
			c=esal*(78/100)
totalsalary=esal+a+b+c
print("@"*96)
print("\t eno is ={}".format(eno))
print("\temp name is ={}".format(ename))
print("\t total salay is= {}".format(totalsalary))
print("End of the program")