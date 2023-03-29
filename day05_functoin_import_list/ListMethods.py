'''
append -> add to the list
clear-> size of the list will be zero
extend -> add multiple to list, use ()
sort -> put in order, ascending or alphabetical order
    sort(reverse= True) for reverse order
reverse -> reverse the list, not order just reverse
copy -> creates nes list on the memory
remove -> reduce the size of the list
pop -> remove the last inserted item on the list
    by the index number specify the item to be removed
insert -> add new element to specific index and shift rest to the right
index -> gives the index number of element in the list
count -> gives count of element in the list
'''

numbers = [10, 20, 30, 40, 50]

numbers.append(60)
#numbers.append(('A', 'B'))

print(numbers)


numbers.clear()

print(numbers)
print(len(numbers))

print("-------------------------------------")

words = ['Cydeo', 'C#', 'C++', 'Ruby']

print(words)

words.extend( ('Java', 'Python', 'Swift') )

print(words)

print("----------------------------------------------")

nums = [100, 20, 55, 15, 0, -1, 30, 40, 16]

nums.sort() # sorted in ascending order

print(nums)

nums2 = [100, 20, 55, 15, 0, -1, 30, 40, 16]
nums2.sort(reverse= True)  # sorted in descending order

print(nums2)

print("--------------------------------------------------")


names = ['Dauren', 'Dzmitry', 'Aidai', 'Faruk', 'Asel', 'Mirigul']

names.reverse()

print(names)

print("--------------------------------------------------")

n1 = [1, 2, 3, 4, 5, 6, 7]
n2 = n1.copy()

#n1.append(100)
print(n1)
print(n2)

print(n1 is n2)


print("--------------------------------------------------")

students = ['Dauren', 'Dzmitry', 'Aidai', 'Faruk', 'Asel', 'Mirigul']

print(students)

students.remove('Dauren')

print(students)

students.remove('Faruk')

print(students)


print("--------------------------------------------------")

l = [50, 100, 150, 200, 250, 300]

l.pop()

print(l)

l.pop()

print(l)

print('------------------------------------------------')

s = ['A', 'B', 'C', 'D', 'E', 'F']

print(s)

s.pop(1)

print(s)

print('------------------------------------------------')

languages = ['Java', 'C#', 'C++', 'Ruby', 'Swift']

languages.insert(0, 'Python')

print(languages)

print('------------------------------------------------')

print( languages.index('C++'))
# print( languages.index('HTML'))

print('------------------------------------------------')

elements = [1,1,1,2,2,2,3,4,5,6,7,8,9,10, 5, 5, 5, 5]

print(elements.count(5))
