N=int(input())
sum1=""
for i in range(N):
    temp=[" " for j in range(N)]
    for k in range(0,N):
        temp[i]="*"
        temp[-1-i]="*"
    for l in temp:
        sum1=sum1+l
    print(sum1)
    sum1=""
    
