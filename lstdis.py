'''n=int(input())
lst=[]
for i in range(n):
	k=(input().split())
	lst.append(k[3])
else:
	print('{}'.format(lst))'''
n=int(input())
a=3.28
arr=[ [],[],[]]
color=[]
for i in range(n):
	line=input().split()
	arr[0].append(line[0])
	arr[1].append(line[1])
	arr[2].append(line[2])
	color.append(line[3])
else:
	print(arr)
	result=[arr[0:3]]
for val in result:
	print(val)
result=[color[0]]

for val in result:
	print(val)


	