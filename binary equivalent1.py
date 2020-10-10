def converttobinary(i):
     binary = [bin(j)[2:] for j in i]
     return binary
def count1and0(binarylist):
    array = []
    for i in binarylist:
        count1 = i.count('1')
        count0 = i.count('0')
        array.append([count1,count0+findzeros(i,arr)])
    return array
def findzeros(i,arr):
    zeros = findmax(arr)-len(i)
    return zeros
def findmax(arr):
    bitlength =[]
    for i in arr:
        binary = bin(i)[2:]
        bitlength.append(len(binary))
    return max(bitlength)
def addcols(countsof1and0):
    rows = len(countsof1and0)
    cols = len(countsof1and0[0])
    sumarr = []
    for i in range(cols):
        sumcol=0
        for j in range(rows):
            sumcol = sumcol+countsof1and0[j][i]
        sumarr.append(sumcol)
    return sumarr 
from itertools import combinations
n = int(input())
arr = list(map(int,input().split()))
count=0
for i in range(1,len(arr)+1):
    combarr = combinations(arr,i)
    for i in list(combarr):
        i = list(i)
        binarylist = converttobinary(i)
        countsof1and0 = count1and0(binarylist)
        columnsum = addcols(countsof1and0)
        if(columnsum[0] == columnsum[1]):
            count+=1
print('0'*findzeros(bin(count)[2:],arr)+bin(count)[2:])
