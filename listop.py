# Declare a list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nInitial list ",l)

# Append
l.append(10)
print("\n1. Appended List :",l)

# Copy
list2 = l.copy()
print("\n2. Copied list is :", list2)

# Clear
list2.clear()
print("\n3. Cleared list :",list2)

# Extend
my_list = l
another_list = [11,12,13] 
my_list.extend(another_list) 
print("\n4. Extended list :",my_list )

# Index
print("\n5. Index of 5 in list is :",l.index(5))

# Count
list2 = [5,5,5,4,3,2,1]
print("\n6. Count of element 5 in list",list2,"is :",list2.count(5))

# Insert
l.insert(5,100)
print("\n7. Inserted 100 at 5th position ",l)

# pop
l.pop()
print("\n8. Popped last element ",l)

# remove
l.remove(100)
print("\n9. Removed 100 from list ",l)

# sort
list2 = [6 , 4, 5, 8, 9, 44, 6]
print("\n10. ",list2,"\nNow Sorted",sorted(list2))

# Reverse
print("\n11. Reversed List :",[ele for ele in reversed(l)])