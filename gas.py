# priject for selection of a number
print("Welcome to shell")
print("*"*45)
print("\t1. Regular")
print("\t2. plus")
print("\t3. Premium")
print("\t4. Desele")
print("*"*45)
a=int(input("Enter your grade= "))
match(a):
	case(1):
		print("You have chossen Regular gas {}".format(a))
	case(2):
		print("You have chossen plus gas {}".format(a))
	case(3):
		print("You have chossen premimu gas {}".format(a))
	case(4):
		print("You have chossen Desele gas {}".format(a))
	case(_):
		print("Thanks for visting see u again")
	print("Enter the shift:")



