no_of_samples,ranges = [int(i) for i in input().split()]
arr = list(map(int,input().split()))
final = []
for i in range(0,ranges):
    start,end = [int(i) for i in input().split()]
    count = 0
    for i in range(0,no_of_samples):
        if(start<=arr[i]<=end):
            count+=1
    final.append(count)
for i in final:
    print(i,end=" ")

            
