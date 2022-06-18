
big=lambda a,b,c: a if (a>b and a>c) else b if (b>c) else c

b=big(21,20,56)
print(b)