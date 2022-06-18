a=int(input("enter the numreater"))
b=int(input("enter denameotar"))
try:
	c=a/b
	s="sunil"
	print(s[10])
	
except ZeroDivisionError as k:
	print(k)
except:
	print("ooops") 

else:
	print(c)
finally:
	print(" visit again")


