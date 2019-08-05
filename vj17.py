    
#a
x1=int(input())
sum=0
temp=x1
while(temp>0):
    c=temp%10
    sum=sum+c**3
    temp=temp//10
if(x1==sum):
    print("yes")
else:
    print("no")
