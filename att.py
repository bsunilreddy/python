n= int(input())
if(n<0):
	print('invalid')
else:
	for i in range(1,11):
		print('{} * {} = {}'.format(n,i,i*n))

s=0
while(n>0):
	d=n%10
	s=s+d
	n=n//10
else:
	print('val',s)
s="sunil"
print('s',s[::-1])

