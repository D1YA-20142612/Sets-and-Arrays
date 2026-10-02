import array as a

arr = a.array('i', [1, 3, 5, 3, 7, 9, 3])
print('Original array:' +str(arr))

print("Number of occurences of the number 3 in the array...\n"
+str(arr.count(3)))

arr.reverse()
print('The reverse of the original array is...')
print(str(arr))
