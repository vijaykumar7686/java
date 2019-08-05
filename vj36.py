    
#a
x1=input()
y=0
for i in range(len(x1)):
    if (x1[i].isalpha() or x1[i].isnumeric() or x1[i]==" "):
      continue
    y=y+1
else:
    print(y)
