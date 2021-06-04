
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
#Note: Python


list=[1,2,3,4,7]
print(list[::2])
print(list[::-1])
print(list*3)
print(type(list))
list1=[7,8,9,0]
list1=list1+list
print(list1)
n=int(input("enter the number search location"))
if n in list:
    print("list index",list.index(n))
else:
    print("list not found")
      
list[3]=90
print("update list",list)
print("remove is",list.remove(2))

l=[]

l1=[int(x)for x in input().split()]
print(l1)
my_list = [1, "Hello", 3.4]
my_list1 = ["mouse", [8, 4, 6], ['a']]
print(my_list)
print(my_list1)
for i in my_list1:
    for j in i:
        print(j)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums)
print(nums[:])
print(nums[2:])
print(nums[2:7])
print(nums[2:-3])
print(nums[::3])
print(nums[::-3])
print(nums[1:7:-3])
print(nums[-3:])
first_five = nums[0:5]
print(first_five)
del nums[3:7]
print(nums)


#list all operation
languages = ['French', 'English']

languages1 = ['Spanish', 'Portuguese']


languages.extend(languages1)

print('Languages List:', languages)
#other way to extent list
gb=languages+languages1
print("gb=",gb)
a = [1, 2]
b = [3, 4]

a[len(a):] = b

# Output: [1, 2, 3, 4]
print('a =', a)
a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)


#list index opetration
#list.index(element, start, end)
#element - the element to be searched
#start (optional) - start searching from this index
#end (optional) - search the element up to this index

vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)
# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']

# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)

# 'i' between 3rd and 5th index is searched
#index = alphabets.index('i', 3, 5)   # Error!
#print('The index of i:', index)



#append operation
animals = ['cat', 'dog', 'rabbit']

# list of wild animals
wild_animals = ['tiger', 'fox']

# appending wild_animals list to the animals list
animals.append(wild_animals)

print('Updated animals list: ', animals)



#insert operation
#list.insert(index, elem)
del alphabets[3]
print(alphabets)
alphabets.insert(3,'o')
print(alphabets)
alphabets.insert(3,wild_animals)
print(alphabets)



#remove operation
animals.remove('dog')
print(animals)


#list count element operation
#list.count(element)
list3=[1,2,3,4,7,8,9,0,3,1,2,8,7,9,4]
cnt=list3.count(7)
print(cnt)

#list pop operation
#list.pop(index)

print("pop value=",list3.pop(7))
print("pop value -3=",list3.pop(-3))

#reverse list operation
list3.reverse()
print(list3)


#sort list operation
list3.sort()
print(list3)
list3.sort(reverse=True)
print(list3)

#list copy operation
newlist=list.copy()
print(newlist)

#list clear operation
newlist.clear()
print(newlist)
