#a
num=int(input())
lst=list(map(int,input().split()))[:num]
lst.sort()
print(*lst,end=" ")
