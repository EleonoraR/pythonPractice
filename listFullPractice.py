mylist1 = ["python", "css", "javascript"]
print(mylist1)

mylist2 = [10, "day", True]
print(mylist2)

item0 = mylist1[0]
item1 = mylist1[1]
item2 = mylist1[2]
print(item0, item1, item2)

last_item = mylist1[-1]
print(last_item)
last_item1 = mylist1[-2]
print(last_item1)
last_item2 = mylist1[-3]
print(last_item2)

# LOOPS IN LIST
for item in mylist2:
  print(f'This is {item}')

if True in mylist2:
  print('Yes')
else:
  print('No')

#len()
print(len(mylist2))

mylist1.append("Hello")
print(mylist1)

mylist1.insert(1, "World")
print(mylist1)

deleted_last_item = mylist1.pop()
print(deleted_last_item)
print(mylist1)

removed_item = mylist2.remove(True)
print(mylist2)

deleted_list = [5,6,9,8]
deleted_i = deleted_list.clear()
print(deleted_list)

numbers_list = [1, 2, 3, 4, 5, 6, 7]
reversed_items = numbers_list.reverse()
print(numbers_list)

sort_items = [5,9,12,56,4,1,2,7,6,3]
sorted_list = sort_items.sort()
print(sort_items)

#Multiple lists 
new_sorted = sorted(sort_items)
print(new_sorted)

#SLICING
list0 = [0]*7
print(list0)

first_list = [1,2,3]
second_list = [4,5,6,7]
added_list = first_list + second_list
print(added_list)

list_original = [1,5,9,15,56,89]
list_slicing = list_original[1:5]
print(list_slicing)
list_slicing = list_original[::-1]
print(list_slicing)


#copying
list_orig = ["apple","coconut","peach"]
#not the best way to copy the list bc it will change 
#original list if you change the copy
list_copy = list_orig
list_copy.append("orange")
print(list_orig)
print(list_copy)
#better way to create a copy 
list_copy0 = list_orig.copy()
list_copy.append("lemon")
print(list_orig)
print(list_copy0)


list_orig1 = ["car","bus","train"]
list_copy1 = list_orig1[:]
list_copy1.append("tractor")
print(list_orig1)
print(list_copy1)

list_orig2 = ["apple","coconut","peach"]
list_copy2 = list(list_orig2)
list_copy2.append("pear")
print(list_orig2)
print(list_copy2)


my_list =[1,2,3,4,5,6,7]
new_list = [i*i for i in my_list]
print(my_list)
print(new_list)
