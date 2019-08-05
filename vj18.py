#a
a,b=map(int,input().split())
for i1 in range(a,b):
  sum=0
  temp=i1
  while(temp>0):
    c=temp%10
    sum=sum+c**3
    temp=temp//10
  if(i1==sum):
    print(sum,end=" ")
