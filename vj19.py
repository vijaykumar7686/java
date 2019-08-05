#a
x1=int(input())
sum=1
if(x1==0):
    print("1")
else:
    for i in range(1,x1+1):
        sum=sum*i 
    print(sum)
