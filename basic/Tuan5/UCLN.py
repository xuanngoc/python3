import stdio

a=stdio.readInt()
b=stdio.readInt()

while b !=0:
	if a>b:
		a -= b
	else:
		b-=a	
if a>b:
	print(a)
else:
	print(b)				