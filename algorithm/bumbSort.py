
arr = list([3,9,10,1,5,99])
print(arr)

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)

arr2 = list([3,9,10,1,5,99])
arr2.sort(reverse=True)
print(arr2)