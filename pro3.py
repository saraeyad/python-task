
arr = []
for i in range(1, 6):
    value = int(input("Please enter the Value of %d Element  : " % i))
    arr.append(value)

arr.sort()

print("The Smallest Element in this List is : ", arr[0])
print("The Largest Element in this List is : ", arr[len(arr)-1])