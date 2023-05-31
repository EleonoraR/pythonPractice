#Section 3. Lesson 21.Numbers int float----saved as binary in memory--------

print(type(2 + 3))
print(type(2 - 3))
print(type(2 * 5))
print(type(2 / 4))

print(2**3)
print(2 // 4)
print(5 % 4)
#Section 3. Lesson 21.Numbers int float-------------------------------

#Section 3. Lesson 22. Math Functions----------------------
print(round(3.7))
print(abs(-20))
#Section 3. Lesson 22. Math Functions--------------------

#Section 3. Lesson 51. Dictionary---------
dictionary = {'a': [1, 2, 3], 'b': 'hello', 'x': True}

my_list = [{
  'a': [1, 2, 3],
  'b': 'hello',
  'x': True
}, {
  'a': [4, 5, 6],
  'b': 'bye',
  'x': False
}]
print(my_list[0]['a'][2])
print(dictionary['a'][1])
#Section 3. Lesson 51. Dictionary---------

#Section 3. Lesson 53. Dictionary Key---------
dictionary_user = {
  123: [1, 2, 3],
  'greet': 'hello',
  'is_Magic': True  #[100]:True ---doesnt work
}

print(dictionary_user[123])
print(dictionary_user['greet'])

#Section 3. Lesson 53. Dictionary Key---------

#Section 3. Lesson 54. Dictionary Methods---------
user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
print(user.get('age', 55))

user2 = dict(name="JohnJohn")
print(user2)

#Section 3. Lesson 54. Dictionary Methods---------

#Section 3. Lesson 55. Dictionary Methods 2---------
print('basket' in user.keys())
print('hello' in user.values())
print(user.items())
user1 = user.copy()

user.clear()
print(user)
print(user1)
print(user1.pop('age'))
print(user1)
print(user1.popitem())
print(user1)
print(user1.update({'age': 55}))
print(user1)
#Section 3. Lesson 55. Dictionary Methods 2---------


#Section 3. Lesson 56. Tuples---------
my_tuple = (1,2,3,4,5,5,5)
print(5 in my_tuple)
user = {
  (1,2): [1,2,3],
  'greet':'hello',
  'age': 20
}
print(user[(1,2)])

#Section 3. Lesson 56. Tuples---------
#Section 3. Lesson 57. Tuples 2---------
new_tuple = my_tuple[1:2]
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

x,y,z, *other = (1,2,3,4,5)
print(other)

#Section 3. Lesson 57. Tuples 2---------

#Section 3. Lesson 58. Sets---------
print('Section 3. Lesson 58. Sets')
my_set = {1,2,3,4,5,5}
my_set.add(100)
my_set.add(2) #will not add it - it is not unique item
print(my_set)
new_set = my_set.copy()
my_set.clear()
print(my_set)
print(list(new_set))

my_list = [1,2,3,8,9]
print(set(my_list))
print(1 in my_list)
print(len(my_list))

#Section 3. Lesson 58. Sets---------

#Section 3. Lesson 59. Sets 2---------
first_set = {4,5}
second_set = {4,5,6,7,8,9,10}

print('Section 3. Lesson 59. Sets 2')
print(first_set.difference(second_set))
print(first_set.discard(5))
print(first_set)
print(first_set.difference_update(second_set))
print(first_set)
print(first_set.intersection(second_set)) # or print(first_set & second_set)
print(first_set.isdisjoint(second_set))
print(first_set.union(second_set))# or print(first_set| second_set)
print(first_set.issubset(second_set))
print(first_set.issuperset(second_set))
print(second_set.issuperset(first_set))

#Section 3. Lesson 59. Sets 2---------

