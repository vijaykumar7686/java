#a
m,n1=map(int,input().split())
for mo in range(m+1,n1):
    if mo>0:
        for i in range(2,mo):
            if mo%i==0:
                break
        else:
            print(mo,end=" ")
