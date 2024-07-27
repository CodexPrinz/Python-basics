ages = [19, 26, 29]
print(ages)

print("--------------> Slice <------------------")
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

ages.append(89)
print(ages)
ages.insert(0,44)
print(ages)
ages.extend(my_list)
print(ages)
ages.remove(44)
print(ages)
del my_list[1]
print(my_list)

print("Ages length: ", len(ages))

print("\n-------------> List Comprehension in Python <---------------")
squares = [n**2 for n in range(1, 8)]
print(squares)


