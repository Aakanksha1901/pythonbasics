#create array (list):
arr = [10,20,30,40,50]
print(arr)

#accessing elements:
arr = [10,20,30,40]

print(arr[0])
print(arr[-1])

#3. Add Elements
#append() → add at end
arr = [10,20,30,40]
arr.append(50)
print(arr)

#insert() → add at specific index
arr = [10,20,30]
arr.insert(1, 15)  # insert 15 at index 1
print(arr)

arr.extend([60,70])
print(arr)

arr.remove(30)
print(arr)
#pop-removes last element
arr.pop()
arr.pop(1)
arr.clear()

arr[2] = 99

len(arr)

#index()
arr.index(40)

#Check if exists
if 50 in arr:
    print("Found")

# Sorting
arr.sort()        # ascending
arr.sort(reverse=True)  # descending

# Reverse
arr.reverse()

# Slicing
arr = [10, 20, 30, 40, 50]

print(arr[1:4])   # 20 30 40
print(arr[:3])    # 10 20 30
print(arr[-3:])   # 30 40 50

#Copy Array
new_arr = arr.copy()

#Concatenate Arrays
arr1 = [10,20,30,40]
arr2 =[70,80]
c = arr1 + arr2
print(c)

#Count Occurrences
arr.count(10)