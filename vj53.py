#s
i=0
Num1 = int(input(""))
S= 0
while(Num1 > 0):
    i= Num1 % 10
    S = S+i
    Num1 = Num1 //10
print(S)
