#a
d1=int(input())
c=1
l=1
p=0
while(d1!=0):
  c=l
  l=p
  p=c+l
  print(p,end=' ')
  d1=d1-1
