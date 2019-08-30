n=int(input())
res=list(map(int,input().split(' ')))
a=max(res)
c=0
for i in res:
    if(a==res[i]):
        c+=1
print(c)