i=int(input())
j=int(input())
m=max(i,j)
while 1:
	if m%i==0 and m%j==0:
		LCM=m
		break
	m=m+1
print(m)
