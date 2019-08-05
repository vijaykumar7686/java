#a1
a1=list(input())
b=" "
for i in range(len(a1)):
    if b in a1:
        a1.remove(b)
print(len(a1))
