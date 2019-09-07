N=int(input())
sum1=""
for i in range(N+1):
    temp=[" " for j in range(N+1)]
    for k in range(0,i):
        temp[k]="*"
    for l in temp:
        sum1=sum1+l
    print(sum1)
    sum1=""
