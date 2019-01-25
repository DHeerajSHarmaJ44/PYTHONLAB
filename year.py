x=int(input("ENTER THE NO. OF SECONDS: "))
p=x//86400
r1=x%86400

q=r1//3600
r2=r1%3600

s=r2//60
r3=s%60
print("days"+str(p)+"hours"+str(s)+"min"+str(r3)+"sec")

