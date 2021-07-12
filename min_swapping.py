###CODE FOR MINIMUM SWAPPING
arr = list(map(int,input().split()))
count=0
i=0
while i < len(arr):
    index=arr[i]-1 #we have to check for the index because exact poition of 4 is 3 that exact poistion of n is n-1
    if arr[i]!=arr[index]:
        arr[i],arr[index]=arr[index],arr[i]
        count+=1
    else:
        i+=1
print(count)
