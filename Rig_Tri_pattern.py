N=int(input())
sum1=""
for i in range(N):
    temp=[" " for j in range(N)]
    for k in range(i+1):
        temp[k]="*"
    for l in temp:
        sum1=sum1+l
    print(sum1)
    sum1=""
    
